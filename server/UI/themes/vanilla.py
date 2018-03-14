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


class LED(ui_base.Component):
    _html = """<div>{source}</div>"""
    _js = """/* LED js */"""
    _css = """/* LED css */"""


class ToggleSwitch(ui_base.Component):
    _html = """<ToggleSwitch html>"""
    _js = """<ToggleSwitch js>"""
    _css = """<ToggleSwitch css>"""


class PushButtonSwitch(ui_base.Component):
    _html = """<PushButtonSwitch html>"""
    _js = """<PushButtonSwitch js>"""
    _css = """<PushButtonSwitch css>"""


class HeartBeat(ui_base.Component):
    _html = """<HeartBeat html>"""
    _js = """<HeartBeat js>"""
    _css = """<HeartBeat css>"""

