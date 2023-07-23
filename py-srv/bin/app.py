from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, RequestHandler
from tornado_sqlalchemy import SQLAlchemy, SessionMixin, as_future

import settings
from model import DogModel

database_url = '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    )

class MainHandler(SessionMixin, RequestHandler):
    def get(self):
        with self.make_session() as session:
            dogs = session.query(DogModel).all()
            results = [
                {
                    "id": dog.id,
                    "breed": dog.breed,
                    "color": dog.color
                } for dog in dogs]

        self.write({'result': results})

define('host', default='0.0.0.0', help='Docker specific address')
define('port', default=8000, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    app = Application([
        ('/dog', MainHandler)
    ], db=SQLAlchemy(database_url))
    http_server = HTTPServer(app)
    http_server.listen(options.port, options.host)
    print(f'Listening on http://{options.host}:{options.port}')
    IOLoop.current().start()

if __name__ == '__main__':
    main()
