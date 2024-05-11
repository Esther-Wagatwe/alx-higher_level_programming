#!/usr/bin/python3
"""
Takes in a letter
Sends POST request to http://0.0.0.0:5000/search_user with letter as parameter.
The letter must be sent in the variable q, if no argument is given, set q=""
"""
import requests
import sys


if __name__ == "__main__":
    """Perform a POST request."""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        response = requests.post(url, data={'q': sys.argv[1]})
    else:
        response = requests.post(url, data={'q': ""})

    try:
        response_json = response.json()
        if response_json == {}:
            print("No result")
        else:
            _id = response_json.get("id")
            name = response_json.get("name")
            print("[{}] {}".format(_id, name))

    except ValueError:
        print("Not a valid JSON")
