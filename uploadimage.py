#python program to host a web with image

import tornado.web
import tornado.ioloop

class basicImageRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
    
class imageUpload(tornado.web.RequestHandler):
    def get(self):
        return
if __name__ == '__main__':

    app = tornado.web.Application([
        (r"/",basicImageRequestHandler),
        (r"/Images/(.*)",tornado.web.StaticFileHandler, {"path":"Images"})
    ])
    port = 9999
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
