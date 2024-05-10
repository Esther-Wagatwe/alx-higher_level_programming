#!/usr/bin/python3
"""
Takes in a URL
Sends a request to the URL
Displays the body of the response (decoded in utf-8).
Manage urllib.error.HTTPError exceptions & print: Error code: HTTP status code
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    """Perform a GET request and display body of response."""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
