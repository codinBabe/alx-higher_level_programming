#!/bin/bash
# A script that takes in a URL and displays all HTTP methods
# the server will accept.

curl -Is "$1" | grep Allow | cut -c 8-
