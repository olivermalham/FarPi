# FarPi

Welcome to FarPi! FarPi is a lightweight server that allows you to remote control hardware attached to a Raspberry Pi via any modern web browser. It is designed so that new virtual control panels can be setup with a minimum of code writing. Although FarPi is written in Python, you don't need any previous python experience, just copy and paste from the examples to get started.

## Quick Start
Running FarPi is very easy. Fire up your Raspberry Pi, open a shell (command line). Navigate to the directory where you installed FarPi and run these commands:

```
cd server/
python far_pi.py all_pi_app
```

Then open a web browser on the Pi, and go to:

```
http://localhost:8888/
```

And you should see the basic panel that lets you contol all the Pi's GPIO pins via toggle switches. Because FarPi runs as a webserver, you can access your control panel from anywhere in the world, as long as you have configured your networking appropriately (too big a subject for this little readme file!).

## How It Works
FarPi is built on top of the Tornado threadless web server. The panel webpage is generated dynamically by the server and sent to the client web browser. The panel on the browser uses a websocket connection back to the server so it can process two way information flow without having to reload the page each time, or use heavyweight REST operations. FarPi can support multiple users on the same panel at the same time, with all panels being updated more or less in real-time. So if User A flicks a toggle switch from off to on, User B will see the same toggle switch move by itself to on. The server reads the state of the hardware periodically, by default every 500ms, and sends to each client a JSON datastructure which the client code uses to update the user interface. Due to the lightweight nature of the system, even a little computer like the Pi should be able to support a few dozen users at the same time (FarPi hasn't been stress tested though, so this may not hold).

## Code Structure
FarPi is split into a number of software components that have specific jobs.

### Application File
The application file holds all the other components together. It serves as the primary configuration file for a control panel. You should have one application file for each control panel that you set up. Here is a basic application file:

```python
# Import the default settings from base_app
from base_app import *

# The User Interface (UI) package defines the interface that the user will see
import UI.example_ui

# The Hardware Abstraction Layer (HAL) package represents the hardware attached to the server
# that the user will interact with via the UI
from HAL.basic_pi import BasicPi

# Number of milliseconds to delay between updates to clients
refresh_ms = 500

# Create the HAL object that interfaces with the hardware
hal = BasicPi()

# Create the object that defines the user interface layout and components
ui = UI.example_ui.ui
```

As you can see, there is not much to it. To customise to your own project, first change the import statement for the HAL module you want to use. Change the refresh delay if you want, but bear in mind that reducing the size of this delay will increase network traffic and load on the Raspberry Pi's processor. Change the line that creates the hal object so it matches the custom HAL you want to use. Finally, change "example_ui" to what ever user interface module you want to use. The HAL and UI modules are decribed below.

### HAL - Hardware Abstraction Layer
The HAL objects create the bridge between the FarPi server and the actual Raspberry Pi hardware. They are all stored in the HAL subdirectory. A base class in hal.py defines the basic functionality. The important files in this folder are:

#### hal.py
This contains the code that defines the basic functionality of the HAL system. If you are going to write your own custom HAL, read the documentation in this file. Your custom HAL should subclass the `HAL` class in here, and your custom components should subclass the `HALComponent` class.


#### basic_pi.py
The file defines a single `HALComponent`, `BasicPiGPIO`, which represents a basic GPIO pin. Direction can be set to in or out, pull up or down and pin number are all configurable. Uses the GPIO module from the RPi library.

The `BasicPi` HAL class defined here just makes available all GPIO pins as outputs with no pull-ups or downs. Uses the BCM pin numbering scheme.

#### virtual.py
The virtual module contains a bunch of HALComponents that provide advanced logic and behaviour. This is only a quick overview, check the source code comments for detailed info. 

`Group` is not a component, it's a helper class that lets you group multiple HALComponent names together. Primarily used to make the HAL object declarations syntax cleaner.

`GroupToggle` lets you switch a group of other HALComponnents between two sets of pre-defined values.

`GeneratorSawTooth` simulates a saw-tooth waveform between a lower and upper bound. Steps by a delta value on every update, so frequemcy is dependant on the refresh interval you set in your app file.

`TripWire` is similar to `GroupToggle`, except that it switches when the value of another HALComponent crosses a threshold value. Could be used for instance to turn on a couple of cooling fans if a temperature sensor passes 30 degrees.

`IfThisThen` is a very powerful virtual component. Using it requires a bit more Python knowledge than the others. Every refresh, it evaluates a "this" expression. If "this" evaluates to True, the "then" expression is executed. If "this" evaluates to False, the "otherwise" expression is executed. All of these expressions are fragments of Python code that are executed using the parent HAL object as the namespace.

#### servo.py
This file provides a small extension to the BasicHAL module so that R/C servoes can be controlled from any GPIO pin. It uses the Python bindings for the PiGPIO library. If you have a project that uses R/C servoes, you'll want to use `ServoHAL` as the base class for your own HAL. Two components are provided:

`Servo` - a basic interface to a single servo on a GPIO pin. Allows the position to be set to any arbitary point, or toggle the position between the two end points. The end points are configurable for maximum flexibility.

`IndexedServo` - similar to the basic Servo component, but is initialise with a list of preset positions. The servo can then be toggle up or down and it will move through the positions defined in the list. It can also be set to any one of the preconfigured positions without stepping through the intermediate positions.

### UI - User Interface

The UI file defines what type of controls to display on your panel, and how those controls connect to your HAL. They are all stored in the `UI` folder by default.  Again, FarPi is designed to make it as simple as possible for non-coders to create a new panel. Here is an example UI definition:

```python
from themes.neon import *

"""
    Very simple panel which just shows one of each vanilla control.
"""

ui = Panel(
        Row(
                LED(pin="bcm00", label="LED"),
                PushButtonSwitch(pin="bcm01", label="Push button"),
                ToggleSwitch(pin="bcm02", action="bcm02.action_toggle", label="Toggle switch")
            ),
        Row(
                LineGauge(source="dummy", label="Line Gauge"),
                ArcGauge(source="dummy", label="Arc Gauge")
        ),
        Row(
                MessageBox()
        ),
        name="FarPi"
)
```

FarPi supports themes which set the "look and feel" of your panel. Currently there is only one theme defined, `neon`. The first line of the UI file tells FarPi that we're using the `neon` theme. If you are interested in writing your own theme, have a look at the `neon.py` file to see how it's done.

Your UI file must create a variable called `ui`, of type `Panel`. Within the `Panel` declaration (everything between the first and last brackets) you declare the control components you want to display, and the keywords you pass these components tell them which part of the HAL to connect to. The `Row` control doesn't do anything except group your controls together into rows in the panel web page.

#### neon.py
The `neon` theme defined the following controls:


`Panel` - This is the container for your control panel. You should always have one, and only one, of these controls.

`Row` - This is non interactive control that simply groups all of the controls that it contains into a single row in your panel web page.

`LED` - A non interactive control that mimics a simple LED attached to a pin. If the pin is "high" (i.e. "on"), the LED is lit, otherwise it's dark. Has a label you can define which is displayed next to the LED.

`PushButtonSwitch` - Simulates a momentary switch, with an LED indicator and a label. As long as the mouse button is held down on the switch in your panel (or touched if using a touch screen), the output pin is set to "high". Resets to "low" (or "off") when released.

`ToggleSwitch` - Looks the same as the `PushButtonSwitch`, but it toggles, so one click turns it to "high", a second click resets it to "low".

`LineGauge` - A simple non interactive bar indicator with a label. It assumes its source has a value between 0.0 and 1.0, and draws a bar representing this value.

`ArcGauge` - A fancier version of `LineGauge`, that draws a semicircular arc instead of a straight bar. It also displays the value of its source as well as a label.

`MessageBox` - A text box for displaying written status messages and other information.

## ToDo
FarPi is still in the very early stages of development, and there is much left to do. Off the top of my head:

1. Sensors - currently FarPi only deals with pins and virtual controls. Need to add support for sensor modules communicating via I2C, SPI and UART. This is going to require help, there are so many different modules available. Base classes to handle the basic comms is top of my list.
2. Improve the Neon theme - I am not a web design guru. Need someone who is to make the default theme as pretty and responsive as possible. Also need to add controls for the user to input a value other than on / off. Rotary knob? Slider?
3. The virtual components need more thorough testing
4. Add more virtual components - random number generator, smooth noise generator, interpolators, different wave form generators (square, sine?)


