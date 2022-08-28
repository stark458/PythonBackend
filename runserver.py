#code snippet to demonstrate the web interface for python programming.

#building apis that does something in the backend.


import tornado
import tornado.web
import tornado.ioloop
import json
class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("var")
        y = "odd" if int(num)%2 else "even"
        self.write(f"the number is {y}")

class resourceParameterHandler(tornado.web.RequestHandler):
    def get(self,name,id):
        self.write(f"hi {name}, welcome to course{id}")

class jsonRequestHandler(tornado.web.RequestHandler):
    def get(self):
        op = open("list.txt")
        #read file and return array of lines.
        content = op.read().splitlines()
        op.close()
        return self.write(json.dumps(content))
    
    #creating a post function
    def post(self):
        var = self.get_argument("animal")
        f = open("list.txt",'a')
        f.write(f"{var}\n")
        f.close()
        return self.write({"message":"posted animal"})

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/isEven",resourceRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)",resourceParameterHandler),
        (r"/animals",jsonRequestHandler)
    ])
    port = 8882
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

