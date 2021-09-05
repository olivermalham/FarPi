from .hal import *
from .virtual import *


class MockGPIO(HALComponent):
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


class MockPiConsole(HALComponent):
    """ HAL component that processes commands sent from the client
    """
    def __init__(self):
        super(HALComponent, self).__init__()
        
    def refresh(self, hal):
        pass

    def action_command(self, command, hal):
        commandParts = command.split()
        hal.message = f"Command received: {command}"
        print(f"Console command received: {commandParts[0]}")
        
        # Deliberatly allow any exceptions thrown here to bubble up
        command_name = f"command_{commandParts[0]}"
        command = getattr(self, command_name)
        command(*commandParts[1:], hal=hal)

    def command_status(self, *args, hal):
        print(f"Received console Status command")
        hal.message = "Status is GREEN"
        

class MarvinMotion(HALComponent):
    """ Component that communicates with the Marvin-core subsystem to handle low level movement 
    """
    def __init__(self):
        super(HALComponent, self).__init__()

        # self._motion_fifo = open("/etc/marvin/motion", "w")
        self._motion_fifo = open("/etc/marvin/motion_test", "w")

        self.head_pitch = 500
        self.head_yaw = 500

        self._motion_packet = {"wheel": [
                                    {"distance":0, "speed": 0.25, "angle": 500}, 
                                    {"distance":0, "speed": 0.25, "angle": 500}, 
                                    {"distance":0, "speed": 0.25}, 
                                    {"distance":0, "speed": 0.25}, 
                                    {"distance":0, "speed": 0.25, "angle": 500}, 
                                    {"distance":0, "speed": 0.25, "angle": 500}], 
                                "head": {"pitch": self.head_pitch, "yaw": self.head_yaw}
                                }
    
    def refresh(self, hal):
        """ Use this to return the status of the current servo positions and motors
        """
        pass

    def action_move(self, hal, **kwargs):
        print(f"Received marvin motion command")
        hal.message = f"Marvin Motion - {kwargs}"
        self._motion_fifo.write("""{"wheel": [{"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25}, {"distance":0, "speed": 0.25}, {"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25, "angle": 500}], "head": {"pitch": 500, "yaw": 500}}""")
        self._motion_fifo.flush()
    
    def action_move_head(self, hal, **kwargs):
        print(f"Received marvin head motion command")
        hal.message = f"Marvin Head Motion - {kwargs}"
        self._motion_packet["head"][kwargs["direction"]] = kwargs["angle"]
        self._update_motion()
        
    def action_stop(self, hal):
        print(f"Received marvin hard stop command")
        hal.message = f"Marvin hard stop!"
        self._motion_fifo.write("""{"wheel": [{"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25}, {"distance":0, "speed": 0.25}, {"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25, "angle": 500}], "head": {"pitch": 500, "yaw": 500}}""")
        self._motion_fifo.flush()
    
    def action_center_head(self, hal):
        print(f"Received marvin head motion command")
        hal.message = f"Marvin Head Center"
        self._motion_fifo.write("""{"wheel": [{"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25}, {"distance":0, "speed": 0.25}, {"distance":0, "speed": 0.25, "angle": 500}, {"distance":0, "speed": 0.25, "angle": 500}], "head": {"pitch": 500, "yaw": 500}}""")
        self._motion_fifo.flush()

    def _update_motion(self):
        print(json.dumps(self._motion_packet))
        self._motion_fifo.write(json.dumps(self._motion_packet))
        self._motion_fifo.flush()



class MockPi(HAL):
    """ Mock HAL class for simulating basic Raspberry Pi hardware.

    """

    def __init__(self):
        # Make sure the HAL system is initialised fully first
        super(MockPi, self).__init__()

        # We're using the BCM pin number scheme

        # Add all the GPIO pins, setting pin number and direction
        self.bcm00 = MockGPIO(pin_number=0, directon=0)
        self.bcm01 = MockGPIO(pin_number=1, directon=0)
        self.bcm02 = MockGPIO(pin_number=2, directon=0)
        self.bcm03 = MockGPIO(pin_number=3, directon=0)
        self.bcm04 = MockGPIO(pin_number=4, directon=0)

        self.wave = GeneratorSquareWave()
        self.commandLine = MockPiConsole()

        self.motion = MarvinMotion()

    def clean_up(self):
        super(MockPi, self).clean_up()
