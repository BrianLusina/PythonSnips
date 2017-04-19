import web

urls = (
    '/', 'index',
)

app = web.application(urls, globals())


def GET():
    greeting = "Hello Mortals!"
    return greeting


class Index(object):
    pass


if __name__ == "__main__":
    app.run()
