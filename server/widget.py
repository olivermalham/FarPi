import os
from rawpi import RawPi
from basicui import BasicUI

# Tornado server settings
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "../html/"),
    "default_filename": "index.html",
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": True,
}

# TCP/IP Port number
port = 8888

# Number of milliseconds to delay between updates to clients
refresh_ms =1000

# Web server paths
paths = {}

# Hardware Abstraction Layer to use
hal = RawPi()

# Module that defines the user interface layout and components to use
ui = BasicUI()
