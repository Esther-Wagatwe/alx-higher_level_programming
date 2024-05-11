#!/usr/bin/python3
"""
takes in a URL
Sends a request to the URL
Displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    """Perform a GET request that retrieves X-Request-Id header value."""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers["X-Request-Id"])
