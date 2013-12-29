import routing
import web

def wsgiHandler():
    return web.application(routing.urls, globals(), autoreload=False).wsgifunc()

if __name__ == "__main__":
    app = web.application(routing.urls, globals())
    app.run()