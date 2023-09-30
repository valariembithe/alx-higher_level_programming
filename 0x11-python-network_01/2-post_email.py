#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse

"""
    sends a POST request to the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
