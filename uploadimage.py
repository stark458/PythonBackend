#python program to host a web with image

import tornado.web
import tornado.ioloop

class basicImageRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index_image.html')
    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f'Images/{f.filename}','wb')
            fh.write(f.body)
            fh.close()
        self.write(f"'http://localhost:9999/Images/{f.filename}'")


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
