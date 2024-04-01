#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import requests
import sys


if __name__ == "__main__":
    alpha = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': alpha}
    res = requests.post(url, data=data)

    try:
        parsed_res = res.json()
        if parsed_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_res.get(
                "id"),parsed_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
