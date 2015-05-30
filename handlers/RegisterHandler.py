from handlers.BaseHandler import BaseHandler


class RegisterHandler(BaseHandler):
    def get(self):
        try:
            errormessage = self.get_argument("error")
        except:
            errormessage = ""
        self.render("static/register.html", errormessage = errormessage)

    def register(self, password, username, email):
        username = username
        password = password
        email = email
        print(username)
        print(password)
        print(email)
        return True

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        email    = self.get_argument("email", "")
        new = self.register(password, username, email)
