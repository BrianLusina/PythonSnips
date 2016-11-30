import web

urls = (
    '/', 'index',
)

app = web.application(urls, globals())


class Index(object):
    def GET(self):
        greeting = "Hello Mortals!"
        return greeting


if __name__ == "__main__":
    app.run()
