from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
    <html><body>
    <h1>qmacro-contextual</h1>
    <p>
    This app hosts <strong>Gmail contextual gadget</strong> resources. See the blog post
    <a href='http://www.pipetree.com/qmacro/blog/2010/06/getting-started-with-gmail-contextual-gadgets/'>Getting Started with Gmail Contextual Gadgets</a> and <a href='http://github.com/qmacro/qmacro-contextual'>this project on Github</a>.
    </p>
    </body></html>
    """)

def main():
  application = webapp.WSGIApplication([
    ('/', MainHandler),
  ], debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
