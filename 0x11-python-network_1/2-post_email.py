#!/usr/bin/python3
"""
Takes in a URL and an email
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response (decoded-utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """Send a post request."""
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print(html.decode('utf-8'))
