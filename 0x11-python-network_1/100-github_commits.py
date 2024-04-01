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
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repo)

    params = {'per_page': 10}
    res = requests.get(url, params=params)
    commits = res.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
