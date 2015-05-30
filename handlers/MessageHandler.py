import tornado.web
from handlers.BaseHandler import BaseHandler

class MessageHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.current_user.replace("\"", "")
        self.render("static/index.html", username=username)