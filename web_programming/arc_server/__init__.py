from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

# todo: python 2.x compatibility import

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
  {}
  </pre>
'''


class ArcHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send a 200 ok response
        self.send_response(200)

        # send headers
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        # write the response
        msg = form.format("\n".join(memory))

        # this will return a response with the path back to the client
        self.wfile.write(msg.encode())

    def do_POST(self):
        """
        Handles post requests to the server
        """
        length = int(self.headers.get("Content-length", 0))
        data = self.rfile.read(length).decode()

        message = parse_qs(data)["message"][0]

        # escape characters
        message = message.replace("<", "&lt;")

        # store in memory
        memory.append(message)

        # sends a redirect to root page
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address=server_address, RequestHandlerClass=ArcHandler)
    print("listening on port 8000")
    httpd.serve_forever()
