"""
Simple sample of a url shortening server that gets requests from a client with information about the
 long url the client would like to shorten and the short url they would like to shorten it to.
 This server then checks if the long url already exists with requests module and if it does stores the
 short url as a key and long url as a value in a dictionary.
 
 If it does not exist a 404 response is returned to the client

 This server is intended to serve three kinds of requests:

  * A GET request to the / (root) path.  The server returns a form allowing
    the user to submit a new name/URI pairing.  The form also includes a
    listing of all the known pairings.
  * A POST request containing "longuri" and "shortname" fields.  The server
    checks that the URI is valid (by requesting it), and if so, stores the
    mapping from shortname to longuri in its dictionary.  The server then
    redirects back to the root path.
  * A GET request whose path contains a short name.  The server looks up
    that short name in its dictionary and redirects to the corresponding
    long URI.

"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs, unquote

import requests

memory = {}

form = '''<!DOCTYPE html>
<title>Bookmark Server</title>
<form method="POST">
    <label>Long URI:
        <input name="longuri">
    </label>
    <br>
    <label>Short name:
        <input name="shortname">
    </label>
    <br>
    <button type="submit">Save it!</button>
</form>
<p>URIs I know about:
<pre>
{}
</pre>
'''


def check_uri(uri, timeout=5):
    """
    Checks if a uri returns response of 200 if it is requested
    Will return True if the response is 200, false otherwise
    :param uri: URI to request
    :param timeout: how long to return False, if we do not get a response
    :return: True/False
    :rtype: bool
    """
    try:
        r = requests.get(url=uri, timeout=timeout)
        return r.status_code == 200
    except (requests.ConnectTimeout, requests.RequestException):
        return False


class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
    """
    Handles concurrency
    """


class Shortener(BaseHTTPRequestHandler):
    """
    Addition of ThreadingMixin allows for the handler class to be concurrent
    """

    def do_GET(self):
        """
        Handles GET requests from client, this request will either be for root path /  or for /some-name
        handle this by removing the / from the request using a string slice
        """
        name = unquote(self.path[1:])

        # check if the name is not None
        if name:
            if name in memory:
                # if the name exists in memory, send a 303 redirect to the requested url
                self.send_response(303)
                self.send_header("Location", memory[name])
                self.end_headers()
            else:
                # the name does not exist in memory, send a 404 response
                self.send_response(404)
                self.send_header("Content-type", "text/plain; charset=utf-8")
                self.end_headers()

                self.wfile.write("I don't know {}".format(name).encode())
        else:
            # the name is None, which means this is the root path, thus we send the form
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # list the known associations in the form
            known = "\n".join("{} : {}".format(key, memory[key]) for key in sorted(memory.keys()))
            self.wfile.write(form.format(known).encode())

    def do_POST(self):
        """
        Handles POST requests from client. In this case will get the long uri and short uri and check
        if the short uri is in memory, perform a request to check if the uri exists and return a response
        to the client
        """
        # DECODE
        length = int(self.headers.get("Content-length", 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)
        longuri = params["longuri"][0]
        shorturi = params["shorturi"][0]

        if check_uri(longuri):
            # this uri exists, thus we store it in memory
            memory[shorturi] = longuri

            # redirect to the root page
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()

        else:
            # the uri could not be found
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()

            self.wfile.write("{} does not exist".format(longuri).encode())


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = ThreadHTTPServer(server_address=server_address, RequestHandlerClass=Shortener)
    print("listening on {}".format(httpd.server_address))
    httpd.serve_forever()
