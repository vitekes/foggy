import tornado.ioloop
import tornado.web


from handlers.BaseHandler import BaseHandler

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.current_user.replace("\"", "")
        self.render("static/home.html", username=username)