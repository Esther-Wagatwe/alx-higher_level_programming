#!/user/bin/python3
"""
Takes your GitHub credentials (username and password)
Uses the GitHub API to display your id.
"""
import sys
import requests


if __name__ == "__main__":
    """Authenticating requests."""
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    authentication = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url, auth=authentication)
    print(response.json.get("id"))
