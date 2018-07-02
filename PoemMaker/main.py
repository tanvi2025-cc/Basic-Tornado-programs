#Tornado libraries
import tornado.ioloop
import tornado.web
#import tornado.application
import os.path
#Template path
#template_path=os.path.join(os.path.dirname(__file__),templates)
#Controller class
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
        difference=noun3)


if __name__=="__main__":
    app = tornado.web.Application(
    handlers=[(r'/', MainHandler), (r'/poem', PoemPageHandler)],
    template_path=os.path.join(os.path.dirname(__file__), "templates")
    ) 
    portNumber=str(8888)
    app.listen(portNumber)
    tornado.ioloop.IOLoop.instance().start()
    