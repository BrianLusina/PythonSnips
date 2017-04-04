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

import requests
import http.server
from urllib.parse import parse_qs, unquote

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
    r = requests.get(url=uri, timeout=timeout)
    return True if r.status_code == 200 else False
