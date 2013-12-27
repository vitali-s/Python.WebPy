import web


class index:
    def GET(self):
        return web.template.render('presentation\\views', base='layout').signin([])

    def POST(self):
        return "Signed in"

