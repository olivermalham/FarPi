from themes.vanilla import *

ui = Panel(
        HeartBeat(beat="2"),
        LED(pin="bcm00", label="bcm00"),
        LED(pin="bcm01", label="bcm01"),
        LED(pin="bcm02", label="bcm02")
)

