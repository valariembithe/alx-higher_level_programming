#!/usr/bin/python3
import sys
import urllib.request
""" sends a request to the URL and displays the value of the X-Request-Id variable"""


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
