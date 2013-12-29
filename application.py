import routing
import web

def wsgi():
    return web.application(routing.urls, globals(), autoreload=False).wsgifunc()

if __name__ == "__main__":
    app = web.application(routing.urls, globals())
    app.run()