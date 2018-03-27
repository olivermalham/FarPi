from hal import *
import pigpio


class Servo(HALComponent):
    """ Simple component for controlling a servo on any GPIO pin.

    Uses DMA to generate accurate PWM signals, via the pigpio library.
    """
    def __init__(self, pin=1, start=0.0, lower=1000, upper=2000, *args, **kwargs):
        super(Servo, self).__init__(*args, **kwargs)
        self._pin_number = pin
        # State should be between 0 and 1.0
        self.state = start
        self._lower_bound = lower
        self._upper_bound = upper

    def refresh(self):
        # TODO:
        pass

    def action_toggle(self, hal):
        """ Toggle the servo position between the two end points.

        :param hal:
        :return:
        """
        hal.message = "Servo action_toggle now:{}".format(self.state)

        if self.state < 0.5:
            hal.pi.set_servo_pulsewidth(self._pin_number, self._lower_bound)
            self.state = 1.0
        else:
            hal.pi.set_servo_pulsewidth(self._pin_number, self._upper_bound)
            self.state = 0.0

    def action_set(self, value, hal):
        """ Move the servo to any arbitrary position between the two endpoints.

        :param value:
        :param hal:
        :return:
        """
        self.state = value
        hal.message = "Servo action_set now:{}".format(self.state)
        pulse = self.state * (self._upper_bound - self._lower_bound) + self._lower_bound
        hal.pi.set_servo_pulsewidth(self._pin_number, pulse)


class ServoHAL(HAL):
    """ Slightly more specialised HAL that uses pigio for multi-channel servo control.

    Note that the pigpio daemon needs to be running on the localhost, port 7777.

    """
    def __init__(self, *args, **kwargs):
        super(ServoHAL, self).__init__(*args, **kwargs)
        self.pi = pigpio.pi('localhost', 7777)

        self.servo1 = Servo(pin=3)

    def clean_up(self):
        pass

