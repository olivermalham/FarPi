import serial
from time import sleep
from .hal import *
from .virtual import *
from .servo_lib.lewansoul_lx16a import ServoController

# UART serial port for servo bus
SERVO_SERIAL_PORT = '/dev/serial0'

# Constants that define servo bus ids for each function
HEAD_PITCH = 5
HEAD_YAW = 6
WHEEL_1 = 1
WHEEL_2 = 2
WHEEL_5 = 3
WHEEL_6 = 4


class MarvinGPIO(HALComponent):
    """ Basic GPIO pin.

    """
    def __init__(self, pin_number=1, direction=True, pull=None, *args, **kwargs):
        super(HALComponent, self).__init__()
        self.state = False
        self._pin_number = pin_number
        self._direction = direction

    def refresh(self, hal):
        # self.state = not self.state
        # if self._direction:
        #    self.state = state
        pass

    def action_toggle(self, hal):
        self.state = not self.state
        hal.message = f"Pin {self._pin_number} toggled; now:{self.state}"

    def action_set(self, value, hal):
        hal.message = "BasicPiGPIO action_set value:{}".format(value)
        self.state = bool(value)


class MarvinConsole(HALComponent):
    """ HAL component that processes commands sent from the client
    """
    def __init__(self):
        super(HALComponent, self).__init__()
        
    def refresh(self, hal):
        pass

    def action_command(self, command, hal):
        command_parts = command.split()
        hal.message = f"Command received: {command}"
        print(f"Console command received: {command_parts[0]}")
        
        # Deliberately allow any exceptions thrown here to bubble up
        command_name = f"command_{command_parts[0]}"
        command = getattr(self, command_name)
        command(*command_parts[1:], hal=hal)

    def command_status(self, *args, hal):
        """ Example command method that is exposed to the client """
        print(f"Received console Status command")
        hal.message = "Status is GREEN"
        

class MarvinMotion(HALComponent):
    """ Component that communicates with the Marvin-core subsystem to handle low level movement 
    """
    def __init__(self):
        super(HALComponent, self).__init__()

        # self._motion_fifo = open("/etc/marvin/motion", "w")
        # self._motion_fifo = open("/etc/marvin/motion_test", "w")

        self._motion_packet = { "move": {"distance":0, "speed": 0.0},
                                "turn": {"angle":0, "speed": 0.0}, 
                                "head": {"pitch": 0, "yaw": 0},
                                "action": None
                                }
        self.servo_controller = ServoController(
            serial.Serial(SERVO_SERIAL_PORT, 115200, timeout=0.2),
            timeout=0.5
        )
    
    def refresh(self, hal):
        """ Use this to return the status of the current servo positions and motors
        """
        pass

    def action_move(self, hal, **kwargs):
        print(f"Received marvin motion command")
        hal.message = f"Marvin Motion - {kwargs}"
        self._motion_packet["move"]["distance"] = int(kwargs["distance"])
        self._motion_packet["move"]["speed"] = int(kwargs["speed"])
        self._update_motors()
    
    def action_turn(self, hal, **kwargs):
        print(f"Received marvin motion command")
        hal.message = f"Marvin Motion - {kwargs}"
        self._motion_packet["turn"]["angle"] = int(kwargs["angle"])
        self._motion_packet["turn"]["speed"] = int(kwargs["speed"])
        self._update_motors()

    def action_head_yaw(self, hal, **kwargs):
        print(f"Received marvin head yaw command")
        angle = int(kwargs["angle"])
        hal.message = f"Marvin Head Yaw f{angle} degrees"
        self.servo_controller.move(HEAD_YAW, angle, 1)
        sleep(0.1)

    def action_head_pitch(self, hal, **kwargs):
        print(f"Received marvin head pitch command")
        angle = int(kwargs["angle"])
        hal.message = f"Marvin Head Pitch f{angle} degrees"
        self.servo_controller.move(HEAD_PITCH, angle, 1)
        sleep(0.1)
        
    def action_stop(self, hal, **kwargs):
        print(f"Received marvin hard stop command")
        hal.message = f"Marvin hard stop!"
        self._motion_packet["action"] = "hard_stop"
        self._update_motors()
    
    def action_center_head(self, hal):
        print(f"Received marvin head motion command")
        hal.message = f"Marvin Head Center"
        self.servo_controller.move_prepare(HEAD_PITCH, 500, 2)
        sleep(0.1)
        self.servo_controller.move_prepare(HEAD_YAW, 500, 2)
        sleep(0.1)
        self.servo_controller.move_start(HEAD_PITCH)
        sleep(0.1)
        self.servo_controller.move_start(HEAD_YAW)
        sleep(0.1)

    def _update_motors(self):
        print(json.dumps(self._motion_packet))


class MarvinHAL(HAL):
    """ Mock HAL class for simulating basic Raspberry Pi hardware.

    """

    def __init__(self):
        # Make sure the HAL system is initialised fully first
        super(MarvinHAL, self).__init__()

        # We're using the BCM pin number scheme

        # Add all the GPIO pins, setting pin number and direction
        self.bcm00 = MarvinGPIO(pin_number=0, directon=0)
        self.bcm01 = MarvinGPIO(pin_number=1, directon=0)
        self.bcm02 = MarvinGPIO(pin_number=2, directon=0)
        self.bcm03 = MarvinGPIO(pin_number=3, directon=0)
        self.bcm04 = MarvinGPIO(pin_number=4, directon=0)

        self.wave = GeneratorSquareWave()
        self.commandLine = MarvinConsole()

        self.motion = MarvinMotion()

    def clean_up(self):
        super(MarvinHAL, self).clean_up()
