import os
import tornado.ioloop
import tornado.web


class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.write('Hello World!!!')


def make_app():
    return tornado.web.Application([
        (r'/hello/world', HelloWorldHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(cur_dir, 'conf/test.yaml')

    from python_swagger_ui import tornado_api_doc
    tornado_api_doc(app, config_path=config_path)

    app.listen(8989)
    tornado.ioloop.IOLoop.current().start()