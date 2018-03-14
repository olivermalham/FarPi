from hal import *
#import RPI


class BasicPiGPIO(HALComponent):
    """ Basic GPIO pin.

    """
    def __init__(self, pin_number=1, directon=1, *args, **kwargs):
        super(HALComponent, self).__init__()
        self.state = False
        self._pin_number = pin_number
        self._direction = directon
        # self._pin = RPI.gpio TODO!

    def refresh(self):
        pass #  TODO: Use RPIO to get the pin value

    def action_toggle(self, msg=""):
        print "BasicPiGPIO action_toggle msg:",msg
        self.state = not self.state


class BasicPi(HAL):
    """ Concrete HAL class for accessing basic Raspberry Pi hardware.

    """

    def __init__(self):
        # Make sure the HAL system is initialised fully first
        super(BasicPi, self).__init__()

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
