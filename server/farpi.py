import sys
import json
import importlib
import logging

import tornado.ioloop
import tornado.web
import tornado.websocket

log = logging.getLogger(__name__)


class FarPiHandler(tornado.websocket.WebSocketHandler):
    """ Core of the FarPi system

    Handles and dispatches messages in-coming from the JS client. Also the kicking off point for refreshing the
    state vector and broadcasting it to all listeners.

    """
    clients = []
    cycle = 0

    def open(self):
        print("WebSocket opened")
        FarPiHandler.clients.append(self)
        
    def on_message(self, message):
        global application
        print "on_message received:", message
        if len(message) > 0:
            try:
                self.despatch(message)
            except Exception as e:
                self.write_message('{"error":"An Error Occurred"}')
 
    def on_close(self):
        print("WebSocket closed")
        FarPiHandler.clients.remove(self)

    def despatch(self, message):
        parsed_msg = json.loads(message)
        print parsed_msg
        # TODO: Need to resolve to a specific HALComponent instance
        if "action" in parsed_msg.keys():
            method_name = parsed_msg["action"]
            method_parameters = parsed_msg["parameters"] if "parameters" in parsed_msg.keys() else {}
            application.hal.action(method_name, **method_parameters)

    @classmethod
    def refresh(cls):
        """ Broadcast the current state to all clients
        """
        application.hal.refresh()
        for client in cls.clients:
            client.write_message(application.hal.serialise())
        cls.cycle += 1


if __name__ == "__main__":
    print "FarPi Server v0.1"

    if len(sys.argv) != 2:
        print "No application specified!"
        exit()

    app_name = sys.argv[1]
    print "Loading Application {}".format(app_name)
    try:
        application = importlib.import_module(app_name)
    except Exception:
        print "Error loading {}!".format(app_name)
        exit()

    urls = [
        (r"/farpi", FarPiHandler),
        (r"/js/(.*)", tornado.web.StaticFileHandler,
         dict(path=application.settings['static_path']+'js/', default_filename='index.html')),
        (r"/css/(.*)", tornado.web.StaticFileHandler,
         dict(path=application.settings['static_path']+'css/', default_filename='index.html')),
        (r"/(.*)", tornado.web.StaticFileHandler,
         dict(path=application.settings['static_path'], default_filename='index.html')),
        ]

    app = tornado.web.Application(urls, **application.settings)
    app.listen(application.port)
    periodic = tornado.ioloop.PeriodicCallback(FarPiHandler.refresh, application.refresh_ms)
    periodic.start()
    print "Server starting on port {}...".format(application.port)
    tornado.ioloop.IOLoop.current().start()
