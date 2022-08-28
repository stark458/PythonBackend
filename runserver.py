#code snippet to demonstrate the web interface for python programming.

#building apis that does something in the backend.


import tornado
import tornado.web
import tornado.ioloop
class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        return "Hello"
class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("var")
        y = "odd" if int(num)%2 else "even"
        self.write(f"the number is {y}")

class resourceParameterHandler(tornado.web.RequestHandler):
    def get(self,name,id):
        self.write(f"hi {name}, welcome to course{id}")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/isEven",resourceRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)",resourceParameterHandler)
    ])
    port = 8882
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

