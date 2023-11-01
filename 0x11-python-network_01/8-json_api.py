#!/usr/bin/python3
"""
     script that takes in a letter 
     sends a POST request to http://0.0.0.0:5000/search_user 
     with the letter as a parameter.
"""


import requests
import sys
if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": letter} 

    r = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        response = r.json
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid json")