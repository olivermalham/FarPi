import os

# The User Interface (UI) package defines the interface that the user will see
import UI.basic_ui

# The Hardware Abstraction Layer (HAL) package represents the hardware attached to the server
# that the user will interact with via the UI
from HAL.basic_pi import BasicPi

# Tornado server settings
# TODO: This needs to be cleaned up
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "../html/"),
    "default_filename": "index.html",
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": True,
}

# The TCP/IP Port number that the server will listen on
port = 8888

# Number of milliseconds to delay between updates to clients
refresh_ms = 500

# Web server paths
paths = {}

# Create the HAL object that interfaces with the hardware
hal = BasicPi()

# Create the object that defines the user interface layout and components
ui = UI.basic_ui.ui
