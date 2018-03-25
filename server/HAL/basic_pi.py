from hal import *
from RPi import GPIO


class BasicPiGPIO(HALComponent):
    """ Basic GPIO pin.

    """
    def __init__(self, pin_number=1, direction=1, *args, **kwargs):
        super(HALComponent, self).__init__()
        self.state = False
        self._pin_number = pin_number
        self._direction = direction

    def refresh(self):
        if self._direction == GPIO.IN:
            self.state = GPIO.input(self._pin_number)

    def action_toggle(self, hal):
        self.state = not self.state
        hal.message = "BasicPiGPIO action_toggle now:{}".format(self.state)
        GPIO.output(self._pin_number, self.state)

    def action_set(self, value, hal):
        hal.message = "BasicPiGPIO action_set value:{}".format(value)
        self.state = bool(value)
        GPIO.output(self._pin_number, self.state)

class DummySensor(HALComponent):
    """ Dummy sensor provides a gradual ramp up of a value.  Resets to zero once it passes 1.0.

    """
    def __init__(self, delta=0.1, *args, **kwargs):
        super(HALComponent, self).__init__()
        self.state = 0.0
        self.delta = delta

    def refresh(self):
        self.state += self.delta
        if self.state > 1.0:
            self.state = 0.0

class BasicPi(HAL):
    """ Concrete HAL class for accessing basic Raspberry Pi hardware.

    """

    def __init__(self):
        # Make sure the HAL system is initialised fully first
        super(BasicPi, self).__init__()

        # We're using the BCM pin number scheme
        GPIO.setmode(GPIO.BCM)

        # Add all the GPIO pins, setting pin number and direction
        self.bcm00 = BasicPiGPIO(pin_number=0, directon=0)
        self.bcm01 = BasicPiGPIO(pin_number=1, directon=0)
        self.bcm02 = BasicPiGPIO(pin_number=2, directon=0)
        self.bcm03 = BasicPiGPIO(pin_number=3, directon=0)

        self.bcm04 = BasicPiGPIO(pin_number=4, directon=0)
        self.bcm05 = BasicPiGPIO(pin_number=5, directon=0)
        self.bcm06 = BasicPiGPIO(pin_number=6, directon=0)
        self.bcm07 = BasicPiGPIO(pin_number=7, directon=0)

        self.bcm08 = BasicPiGPIO(pin_number=8, directon=0)
        self.bcm09 = BasicPiGPIO(pin_number=9, directon=0)
        self.bcm10 = BasicPiGPIO(pin_number=10, directon=0)
        self.bcm11 = BasicPiGPIO(pin_number=11, directon=0)

        self.bcm12 = BasicPiGPIO(pin_number=12, directon=0)
        self.bcm13 = BasicPiGPIO(pin_number=13, directon=0)
        self.bcm14 = BasicPiGPIO(pin_number=14, directon=0)
        self.bcm15 = BasicPiGPIO(pin_number=15, directon=0)

        self.bcm16 = BasicPiGPIO(pin_number=16, directon=0)
        self.bcm17 = BasicPiGPIO(pin_number=17, directon=0)
        self.bcm18 = BasicPiGPIO(pin_number=18, directon=0)
        self.bcm19 = BasicPiGPIO(pin_number=19, directon=0)

        self.bcm20 = BasicPiGPIO(pin_number=20, directon=0)
        self.bcm21 = BasicPiGPIO(pin_number=21, directon=0)
        self.bcm22 = BasicPiGPIO(pin_number=22, directon=0)
        self.bcm23 = BasicPiGPIO(pin_number=23, directon=0)

        self.bcm24 = BasicPiGPIO(pin_number=24, directon=0)
        self.bcm25 = BasicPiGPIO(pin_number=25, directon=0)
        self.bcm26 = BasicPiGPIO(pin_number=26, directon=0)
        self.bcm27 = BasicPiGPIO(pin_number=27, directon=0)

        self.dummy = DummySensor(delta=0.1)

    def clean_up(self):
        super(BasicPi, self).clean_up()
        GPIO.cleanup()
