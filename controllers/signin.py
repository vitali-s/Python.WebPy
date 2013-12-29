import routes
import web


class index:
    def GET(self):
        return web.template.render('views', base='layout').signin([])

    def POST(self):
        return web.seeother(routes.home)

