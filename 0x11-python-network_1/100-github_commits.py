#!/usr/bin/python3
"""
evaluates candidates applying for a back-end position
with multiple technical challenges
"""
import requests
import sys


if __name__ == "__main__":
    """Perform a GET operation."""
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}".format(owner_name, repo_name)
    response = requests.get(url)
    response_json = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                  response_json[i].get("sha"),
                  response_json.get("commit").get("author").get("name")))

    except IndexError:
        pass
