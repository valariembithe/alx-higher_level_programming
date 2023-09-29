#!/usr/bin/python3
"""
    sends a request to the URL 
    displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Requests-Id"))