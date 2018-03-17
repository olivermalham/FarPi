from themes.vanilla import *

ui = Panel(
        LED(pin="bcm00", label="bcm00"),
        PushButtonSwitch(pin="bcm01", label="bcm01"),
        ToggleSwitch(pin="bcm02", action="bcm02.action_toggle", label="bcm02"),
        LineGauge(source="dummy", label="Line Gauge")
)
