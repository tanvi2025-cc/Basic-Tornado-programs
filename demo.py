#Tornado import statements
import tornado.ioloop
import tornado.web
import os.path

#web server
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')

#Setting the url
application=tornado.web.Application([
    (r"/",MainHandler)
])
#Starting the server
if __name__=='__main__':
    PortNumber = str(8888)
    print(r'Server Running at http://localhost:' + PortNumber + r'/')
    print(r'To close press ctrl + c')
    application.listen(PortNumber)
    tornado.ioloop.IOLoop.instance().start()




