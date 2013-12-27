import web
import routing


def wsgi():
    return web.application(routing.urls, globals(), autoreload=False).wsgifunc()

if __name__ == "__main__":
    app = web.application(routing.urls, globals())
    app.run()