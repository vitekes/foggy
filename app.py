import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.web import StaticFileHandler
import settings
import tornado.websocket
from tornado.options import define, options
import signal

from handlers.BaseHandler import BaseHandler
from handlers.LoginHandler import LoginHandler
from handlers.LogoutHandler import LogoutHandler
from handlers.WebsocketHandler import WebSocketHandler
from handlers.MainHandler import MainHandler
from handlers.MessageHandler import MessageHandler
from handlers.RegisterHandler import RegisterHandler

def signal_handler(signum, frame):
    tornado.ioloop.IOLoop.instance().stop()

signal.signal(signal.SIGINT, signal_handler)


class Application(tornado.web.Application):
    def __init__(self):
        import settings
        login_handler = LoginHandler
        logout_handler = LogoutHandler
        register_handler = RegisterHandler
        main_handler = MainHandler
        websocket_handler = WebSocketHandler
        messages_handler = MessageHandler

        handlers = [
            (r"/", main_handler),
            (r"/login/", login_handler),
            (r"/logout/", logout_handler),
            (r"/register", register_handler),
            (r'/ws', websocket_handler),
            (r'/msg', messages_handler),
            (r'/js/(.*)', StaticFileHandler, {"path" : r"static/js"}),
            (r'/css/(.*)', StaticFileHandler, {"path" : r"static/css"}),
            (r'/modules/(.*)', StaticFileHandler, {"path" : r"static/modules"}),
            (r'/demo/(.*)', StaticFileHandler, {"path" : r"static/demo"}),
            (r'/images/(.*)', StaticFileHandler, {"path": r"static/images"}),
        ]
        settings = {
            "template_path":settings.TEMPLATE_PATH,
            "static_path":settings.STATIC_PATH,
            "debug":settings.DEBUG,
            "cookie_secret": settings.COOKIE_SECRET,
            "login_url": "/login/"
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    print(settings.STATIC_PATH)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    # http_server.listen(options.port)
    http_server.listen(port=8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        tornado.ioloop.IOLoop.instance().stop()