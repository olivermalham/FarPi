""" Mockip UI definition file to try and work out how to build the system.

I sant this to be as simple and intuitive as possible, whilst also being
powerful and easily extensible. It also needs to be pure python.

Themes is a directory holding a bunch of python packages.
ui is the GUI instance that the server is looking for. When converted to a
string it should output an HTML page with embedded hooks for the JavaScript
parts to interact with.

I like the relative elegance of nested function calls, as demoed below, 
for capturing the hierarchial structure of HTML.

The various GUI components will inherit from one of  a pair of base classes,
one for containers, the other for components.

All UI classes implement the __call__() method. Containers use *args to 
iterate through all children, simply outputting whatever they evaluate to 
when converted to strings, wrapped with a preamble and postamble(?).

Componets are simpler, and just return a fragment of HTML when called. Just
use simple .format() call with the **kwargs dictionary.

As well as outputting HTML, there should also be hooks for generating 
additional JavaScript and CSS for appending to the primary JS and CSS files.
By augmenting these static files rather than creating new ones it reduces the 
number of web requests that have to be made.

Example:
import themes.vanilla.*
ui = panel(
            row(
                horizontal_bar(value="bcm23", label="Temperatuee"), 
                toggle_switch(value"bcm01", label="Fan")
                ),
            row(
                dial_meter(value="bcm12", label="Volts")
                )
               )
"""

class Container(object):

    _prefix="""<div>(prefix)"""
    _postfix="""</div>(postfix)"""
    _child_prefix="""<span>(child prefix)"""
    _child_postfix="""</span>(child postfix)"""

    _javascript = ""
    _css = ""

    @classmethod
    def __call__(cls, *args, **kwargs):
        """ wraps all child element HTML in it's own.
        """
        html = cls._prefix.format(**kwargs)
        js = cls._javascript.format(**kwargs)
        css = cls._css.format(**kwargs)
        
        for child in args:
            html += cls._child_prefix.format(**kwargs) + child[0] + cls._child_postfix.format(**kwargs)
            js += child[1]
            css += child[2]
            
        html += cls._postfix.format(**kwargs)
        
        return html, js, css


class Component(object):

    _html = """<some html>"""
    _js = """<some js>"""
    _css = """<some css>"""
    
    @classmethod
    def __call__(cls, *args, **kwargs):
        return cls._html.format(**kwargs), cls._js.format(**kwargs), cls._css.format(**kwargs),

