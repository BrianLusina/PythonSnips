from http.server import HTTPServer, BaseHTTPRequestHandler
# todo: python 2.x compatibility import


class ArcHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send a 200 ok response
        self.send_response(200)

        # send headers
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        # write the response
        # self.wfile.write("Hello from Arc Server\n".encode())

        # this will return a response with the path back to the client
        self.wfile.write(self.path[1:].encode())


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address=server_address, RequestHandlerClass=ArcHandler)
    print("listening on port 8000")
    httpd.serve_forever()
