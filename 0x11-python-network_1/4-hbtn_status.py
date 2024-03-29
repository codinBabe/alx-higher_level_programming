#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    d = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(d), d))
