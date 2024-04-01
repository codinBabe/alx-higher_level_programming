#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    auth = HTTPBasicAuth(username, password)
    res = requests.get(url, auth=auth)
    print(res.json().get("id"))
