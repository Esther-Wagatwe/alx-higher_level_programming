#!/usr/bin/python3
"""
takes in a URL and an email address
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    """Send a POST request."""
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    response = request.post(url, data=email)
    print(response.text)
