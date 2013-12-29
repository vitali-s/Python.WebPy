import web


class index:
    def GET(self):
        return web.template.render('views', base='layout').home()
