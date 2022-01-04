from collections import namedtuple
import serial
from time import sleep
from .hal import *
from .virtual import *
from .servo_lib.lewansoul_lx16a import ServoController

# UART serial port for servo bus
SERVO_SERIAL_PORT = '/dev/serial0'

# Constants that define servo bus ids for each function
WHEEL_1 = 1
WHEEL_2 = 2
WHEEL_5 = 3
WHEEL_6 = 4
HEAD_YAW = 5
HEAD_PITCH = 6

ServoCalib = namedtuple("ServoCalib", "scale origin limit_low limit_high")


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

        # Servo calibration settings for converting from degrees to servo units
        # Note that entry 0 is None as we're mapping servo id's here, which start at 1
        # Limits are in degrees, not servo units. Origin is the offset corresponding to
        # zero degrees. Making the scale value negative should reverse the movement
        self.servo_calib = [None,
                            ServoCalib(scale=3.7, origin=500, limit_low=-135.0, limit_high=135.0),
                            ServoCalib(scale=3.7, origin=500, limit_low=-135.0, limit_high=135.0),
                            ServoCalib(scale=3.7, origin=500, limit_low=-135.0, limit_high=135.0),
                            ServoCalib(scale=3.7, origin=500, limit_low=-135.0, limit_high=135.0),
                            ServoCalib(scale=3.7, origin=500, limit_low=-135.0, limit_high=135.0),  # Yaw
                            ServoCalib(scale=3.7, origin=500, limit_low=-41.0, limit_high=41.0)]  # Pitch

        self._servo_controller = ServoController(
            serial.Serial(SERVO_SERIAL_PORT, 115200, timeout=0.2),
            timeout=0.5
        )

        self.head_pitch = self._servo_controller.get_position(HEAD_PITCH)
        self.head_pitch_limits = (350, 650)
        sleep(0.1)
        self.head_yaw = self._servo_controller.get_position(HEAD_YAW)
        self.head_yaw_limits = (0, 1000)
        sleep(0.1)
        self.wheel1_angle = self._servo_controller.get_position(WHEEL_1)
        sleep(0.1)
        self.wheel2_angle = self._servo_controller.get_position(WHEEL_2)
        sleep(0.1)
        self.wheel5_angle = self._servo_controller.get_position(WHEEL_5)
        sleep(0.1)
        self.wheel6_angle = self._servo_controller.get_position(WHEEL_6)
        sleep(0.1)
    
    def refresh(self, hal):
        """ Use this to return the status of the current servo positions and motors
        """
        # TODO: These sleep intervals need to be fixed, this gets called frequently, risk of collision!
        self.head_pitch = self._servo_controller.get_position(HEAD_PITCH)
        sleep(0.1)
        self.head_yaw = self._servo_controller.get_position(HEAD_YAW)
        sleep(0.1)

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
        if "delta" in kwargs:
            angle = self.head_yaw + int(kwargs["delta"])
            time = 100
        else:
            angle = int(kwargs["angle"])
            time = 500

        hal.message = f"Marvin Head Yaw {angle} degrees"
        self._servo_controller.move(HEAD_YAW, self._transform_angle(HEAD_YAW, angle), time)
        sleep(0.1)
        self.head_yaw = angle  # TODO: This should be fetched from the servo dynamically!

    def action_head_pitch(self, hal, **kwargs):
        print(f"Received marvin head pitch command")
        if "delta" in kwargs:
            angle = self.head_pitch + int(kwargs["delta"])
            time = 100
        else:
            angle = int(kwargs["angle"])
            time = 500

        hal.message = f"Marvin Head Pitch {angle} degrees"
        self._servo_controller.move(HEAD_PITCH, self._transform_angle(HEAD_PITCH, angle), time)
        sleep(0.1)
        self.head_pitch = angle  # TODO: This should be fetched from the servo dynamically!
        
    def action_stop(self, hal, **kwargs):
        print(f"Received marvin hard stop command")
        hal.message = f"Marvin hard stop!"
        self._motion_packet["action"] = "hard_stop"
        self._update_motors()
    
    def action_head_center(self, hal):
        print(f"Received marvin head motion command")
        hal.message = f"Marvin Head Center"
        self._servo_controller.move(HEAD_PITCH, self.servo_calib[HEAD_PITCH].origin, 1000)
        sleep(0.1)
        self._servo_controller.move(HEAD_YAW, self.servo_calib[HEAD_YAW].origin, 1000)
        sleep(0.1)
        self.head_yaw = 0
        self.head_pitch = 0

    def _update_motors(self):
        print(json.dumps(self._motion_packet))

    def _transform_angle(self, servo_no, angle):
        """ Convert the given servo position in degrees into servo units. """

        angle = self.servo_calib[servo_no].limit_low if angle < self.servo_calib[servo_no].limit_low else angle
        angle = self.servo_calib[servo_no].limit_high if angle > self.servo_calib[servo_no].limit_high else angle
        angle = self.head_pitch_limits[1] if angle > self.head_pitch_limits[1] else angle
        servo_pos = self.servo_calib[servo_no].origin + (self.servo_calib[servo_no].scale * angle)
        return servo_pos


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
