#!/usr/bin/python3
"""
     script that takes your GitHub credentials (username and password) 
     uses the GitHub API to display your id
"""


import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBAsicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))