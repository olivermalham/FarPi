from hal import *
import pigpio


class Servo(HALComponent):

    def __init__(self, pin=1, start=0.5, lower=1000, upper=2000, *args, **kwargs):
        super(Servo, self).__init__(*args, **kwargs)
        self._pin_number = pin
        # State should be between 0 and 1.0
        self._state = start
        self._lower_bound = lower
        self._upper_bound = upper

    def refresh(self):
        # TODO:
        pass

    def action_toggle(self, hal):
        hal.message = "Servo action_toggle now:{}".format(self._state)

        if self._state < (self._upper_bound - self._lower_bound) + self._lower_bound:
            hal.pi.set_servo_pulsewidth(self._pin_number, self._lower_bound)
            self._state = 0.0
        else:
            hal.pi.set_servo_pulsewidth(self._pin_number, self._upper_bound)
            self._state = 1.0

    def action_set(self, value, hal):
        self._state = value
        hal.message = "Servo action_set now:{}".format(self._state)
        pulse = self._state*(self._upper_bound - self._lower_bound) + self._lower_bound
        hal.pi.set_servo_pulsewidth(self._pin_number, pulse)


class ServoHAL(HAL):
    """ Slightly more specialised HAL that uses pigio for multi-channel servo control.

    """
    def __init__(self, *args, **kwargs):
        super(ServoHAL, self).__init__(*args, **kwargs)
        self.pi = pigpio.pi('localhost', 7777)

        self.servo1 = Servo(pin=3)

    def clean_up(self):
        pass

