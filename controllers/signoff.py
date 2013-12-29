import routes
import web


class index(object):
    def GET(self):
        return web.seeother(routes.default)
