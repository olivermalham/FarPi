from hal import *
from virtual import *


class MockGPIO(HALComponent):
    """ Basic GPIO pin.

    """
    def __init__(self, pin_number=1, direction=True, pull=None, *args, **kwargs):
        super(HALComponent, self).__init__()
        self.state = True
        self._pin_number = pin_number
        self._direction = direction

    def refresh(self, hal):
        pass
#        if self._direction:
#            self.state = state

    def action_toggle(self, hal):
        self.state = not self.state
        hal.message = "BasicPiGPIO action_toggle now:{}".format(self.state)

    def action_set(self, value, hal):
        hal.message = "BasicPiGPIO action_set value:{}".format(value)
        self.state = bool(value)


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

    def clean_up(self):
        super(MockPi, self).clean_up()
