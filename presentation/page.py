import web
 
urls = (
    '/', 'index'
    '/signin/', 'signin',
    '/signoff/', 'signoff',
)
 
class index:
    def get(self):
        return "Hello, world! from python"

def wsgiHandler():
    return web.application(urls, globals(), autoreload=False).wsgifunc()
 
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()