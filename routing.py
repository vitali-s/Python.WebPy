import routes

# controllers_module = controllers.{0}.

urls = (
    routes.default, 'controllers.signin.index',
    routes.signin, 'controllers.signin.index',
    routes.signoff, 'controllers.signoff.index',
    routes.home, 'controllers.home.index'
)