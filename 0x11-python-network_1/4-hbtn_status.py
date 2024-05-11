#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
must use the package requests
"""
import requests


if __name__ == "__main__":
    """Perform a get operation."""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(response.text.__class__))
    print("\t- content: {}".format(response.text))
