import webapp2
import urllib
import time
import os

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        print "Hello '/' !"

class CronPing(webapp2.RequestHandler):
    def get(self):
        urls = os.environ['PINGING_URLS'].split('|')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello Cron!\n\n');
        for i in xrange(len(urls)):
            print(urls[i])
            try:
                response = urllib.urlopen(urls[i]).read()
                self.response.write("Success " + urls[i] + "\n\n")
            except Exception, e:
                self.response.write("Failure " + urls[i] + "\n\n")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/docron', CronPing)
], debug=True)
