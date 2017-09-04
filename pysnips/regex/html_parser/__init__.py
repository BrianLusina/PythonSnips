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

    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data == "\n":
            return
        print(">>> Data")
        print(data)


pyhtmlparser = PyHtmlParser()
pyhtmlparser.feed("".join(input().strip() for _ in range(int(input()))))
pyhtmlparser.close()
