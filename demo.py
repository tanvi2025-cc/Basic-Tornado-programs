#Tornado import statements
import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPClient
import os.path

#web server
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')
#Request Handlers
class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
       self.render('templates/form.html')
    def post(self):
        username = self.get_argument('username')
        designation = self.get_argument('designation')
        self.write("Wow " + username + " you're a " + designation)
  

#Setting the url
application=tornado.web.Application([
    (r"/",MainHandler),
    (r"/form",MyFormHandler)
])
def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body
print(synchronous_fetch('https://google.com'))

#Starting the server
if __name__=='__main__':
    PortNumber = str(8888)
    print(r'Server Running at http://localhost:' + PortNumber + r'/')
    print(r'To close press ctrl + c')
    application.listen(PortNumber)
    tornado.ioloop.IOLoop.instance().start()




