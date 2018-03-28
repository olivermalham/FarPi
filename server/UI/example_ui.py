from themes.neon import *

"""
    Very simple panel which just shows one of each vanilla control.
"""

ui = Panel(
        Row(
                LED(pin="bcm00", label="LED"),
                PushButtonSwitch(pin="bcm01", label="Push button"),
                ToggleSwitch(pin="bcm02", action="bcm02.action_toggle", label="Toggle switch"),
                LineGauge(source="dummy", label="Line Gauge"),
                ArcGauge(source="dummy", min=180, max=360, label="Arc Gauge")
        ),
        Row(
                MessageBox()
        ),
        name="FarPi"
)
