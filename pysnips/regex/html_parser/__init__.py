from html.parser import HTMLParser


class PyHtmlParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

    def handle_endtag(self, tag):
        print("End   : {}".format(tag))

    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))


pyhtmlparser = PyHtmlParser()
pyhtmlparser.feed("".join(input().strip() for _ in range(int(input()))))
