from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
    <html><body>
    <h1>qmacro-contextual</h1>
    <p>This app hosts Gmail contextual gadget resources</p>
    </body></html>
    """)

def main():
  application = webapp.WSGIApplication([
    ('/', MainHandler),
  ], debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
