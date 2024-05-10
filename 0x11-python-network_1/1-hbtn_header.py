#!/usr/bin/python3
"""sends a request a URL and displays the value of the X-Request-Id variable
found in the header of the response."""
import urllib.request
import sys


if __name__ == "__main__":
    """Perform a GET request that retrieves X-Request-Id header value."""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
