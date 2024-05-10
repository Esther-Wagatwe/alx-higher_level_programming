#!/usr/bin/python3
"""
Takes in a URL and an email
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response (decoded-utf-8)
"""
import urllib.request
import sys

if "__name__" == "__main__":
    """Send a post request."""
    url = sys.argv[1]

