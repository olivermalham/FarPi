# Import the default settings from base_app
from base_app import *

# The Hardware Abstraction Layer (HAL) package represents the hardware attached to the server
# that the user will interact with via the UI
from HAL.servo import ServoHAL

# Number of milliseconds to delay between updates to clients
refresh_ms = 500

# Create the HAL object that interfaces with the hardware
hal = ServoHAL()

# Create the object that defines the user interface layout and components
ui = UI.servo_ui.ui
