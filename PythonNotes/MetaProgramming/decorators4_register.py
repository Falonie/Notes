class App(object):
    def __init__(self):
        self.routes = {}

    def route(self, url):
        def register(f):
            self.routes[url] = f
            return f
        return register


app = App()
url1 = app.route('/index/')(lambda x: x)
print(url1)
print(app.routes)