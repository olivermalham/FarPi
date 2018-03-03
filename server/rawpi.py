from hal import HAL, HALComponent
#import RPI


class RawPi_GPIO_Pin(HALComponent):
    """ Basic GPIO input pin.

    """
    def __init__(self, pin_number=1, directon=1, *args, **kwargs):
        super(HALComponent, self).__init__()
        self.state = False
        self._pin_number = pin_number
        self._direction = directon

    def refresh(self):
        print "RawPi_GPIO_Pin refresh"
        self.state = False #  TODO: Use RPIO to get the pin value

    def action_toggle(self, msg=""):
        print "RawPi_GPIO_Pin action_toggle msg:",msg
        self.state = not self.state


class RawPi(HAL):
    """ Concrete HAL class for accessing basic Raspberry Pi hardware.

    """

    def __init__(self):
        # Make sure the HAL system is initialised fully first
        super(RawPi, self).__init__()

        # Add all the GPIO pins, setting pin number and direction
        self.bcm00 = RawPi_GPIO_Pin(pin_number=0, directon=0)
        self.bcm01 = RawPi_GPIO_Pin(pin_number=1, directon=0)
        self.bcm02 = RawPi_GPIO_Pin(pin_number=2, directon=0)
        self.bcm03 = RawPi_GPIO_Pin(pin_number=3, directon=0)

        self.bcm04 = RawPi_GPIO_Pin(pin_number=4, directon=0)
        self.bcm05 = RawPi_GPIO_Pin(pin_number=5, directon=0)
        self.bcm06 = RawPi_GPIO_Pin(pin_number=6, directon=0)
        self.bcm07 = RawPi_GPIO_Pin(pin_number=7, directon=0)

        self.bcm08 = RawPi_GPIO_Pin(pin_number=8, directon=0)
        self.bcm09 = RawPi_GPIO_Pin(pin_number=9, directon=0)
        self.bcm10 = RawPi_GPIO_Pin(pin_number=10, directon=0)
        self.bcm11 = RawPi_GPIO_Pin(pin_number=11, directon=0)

        self.bcm12 = RawPi_GPIO_Pin(pin_number=12, directon=0)
        self.bcm13 = RawPi_GPIO_Pin(pin_number=13, directon=0)
        self.bcm14 = RawPi_GPIO_Pin(pin_number=14, directon=0)
        self.bcm15 = RawPi_GPIO_Pin(pin_number=15, directon=0)

        self.bcm16 = RawPi_GPIO_Pin(pin_number=16, directon=0)
        self.bcm17 = RawPi_GPIO_Pin(pin_number=17, directon=0)
        self.bcm18 = RawPi_GPIO_Pin(pin_number=18, directon=0)
        self.bcm19 = RawPi_GPIO_Pin(pin_number=19, directon=0)

        self.bcm20 = RawPi_GPIO_Pin(pin_number=20, directon=0)
        self.bcm21 = RawPi_GPIO_Pin(pin_number=21, directon=0)
        self.bcm22 = RawPi_GPIO_Pin(pin_number=22, directon=0)
        self.bcm23 = RawPi_GPIO_Pin(pin_number=23, directon=0)

        self.bcm24 = RawPi_GPIO_Pin(pin_number=24, directon=0)
        self.bcm25 = RawPi_GPIO_Pin(pin_number=25, directon=0)
        self.bcm26 = RawPi_GPIO_Pin(pin_number=26, directon=0)
        self.bcm27 = RawPi_GPIO_Pin(pin_number=27, directon=0)
