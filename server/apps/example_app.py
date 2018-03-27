# Import the default settings from base_app
from base_app import *

# The User Interface (UI) package defines the interface that the user will see
import server.UI.example_ui

# The Hardware Abstraction Layer (HAL) package represents the hardware attached to the server
# that the user will interact with via the UI
from server.HAL.basic_pi import BasicPi

# Number of milliseconds to delay between updates to clients
refresh_ms = 500

# Create the HAL object that interfaces with the hardware
hal = BasicPi()

# Create the object that defines the user interface layout and components
ui = server.UI.example_ui.ui
