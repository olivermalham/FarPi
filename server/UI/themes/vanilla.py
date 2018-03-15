from .. import ui_base


class Panel(ui_base.Container):
    """ Basic control console.

    """
    # Opening HTML fragment for the main container
    _prefix="""<!-- Panel -->\n<div>\n"""

    # Closing HTML fragment for the main container
    _postfix="""</div> <!-- End Panel -->\n"""

    # HTML fragment added immediately before each child HTML section
    _child_prefix=""" """

    # HTML fragment added immediately after each child HTML section
    _child_postfix=""" """

    # Javascript template to provide extra functionality not available in the base code. Optional.
    _javascript = ""

    # CSS stylesheet template to provide extra styles if required. Option.
    _css = ""

    # Page template defines the page that will surround the GUI defined by the UI
    # objects. Should be a string, will be run through the Python .format method
    # to replace {far_pi} with the generated control panel.
    _page_template = """
<!doctype html>
<html lang="en">

<head>
    <title>FarPi</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:100" rel="stylesheet">
    <script src="/js/farpi.js"></script>
    <script src="/farpiGUI.js"></script>
    <link rel="stylesheet" href="/css/farpi.css">
    <link rel="stylesheet" href="/farpiGUI.css">
</head>
<body onload="FarPi.onLoad('ws://localhost:8888/farpi');">
<div id="title">- F   a   r   P   i -</div>
<hr />
<center>

{far_pi}

</center>
</body>
</html>
"""


class LED(ui_base.Component):
    _html = """
<div class="LED">
    <div id="LED_{{pin}}">{{label}}</div>
</div>
    """

    _js = """
/* LED js */
console.log("LED {{pin}} JS run");

FarPi.registerCallback(function(){
    var LED_element = document.getElementById("LED_{{pin}}");
    if(FarPi.state["{{pin}}"].state){
        LED_element.style.backgroundColor = "#ff6600";
    } else {
        LED_element.style.backgroundColor = "transparent";
    }
    //console.log("LED update {{pin}}");
});

    """
    _css = """/* LED {{pin}} css */"""


class ToggleSwitch(ui_base.Component):
    _html = """<ToggleSwitch html>"""
    _js = """<ToggleSwitch js>"""
    _css = """<ToggleSwitch css>"""


class PushButtonSwitch(ui_base.Component):
    _html = """<PushButtonSwitch html>"""
    _js = """<PushButtonSwitch js>"""
    _css = """<PushButtonSwitch css>"""


class HeartBeat(ui_base.Component):
    _html = """
<div class="HeartBeat">
    <div id="HeartBeat">Heartbeat</div>
</div>
"""

    _js = """
/* Heartbeat js */
console.log("Heartbeat JS run");

FarPi.registerCallback(function(){
    var heartbeat_element = document.getElementById("HeartBeat");
    if(FarPi.state["cycle"] % {{beat}}){
        heartbeat_element.style.backgroundColor = "#ff6600";
    } else {
        heartbeat_element.style.backgroundColor = "transparent";
    }
    //console.log("Heartbeat update")
});
"""
    _css = """/* Heartbeat css */"""

