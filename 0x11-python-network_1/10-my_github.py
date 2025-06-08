#!/usr/bin/python3
'''a Python script that takes your GitHub credenand uses
    the GitHub API to display your id
'''

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    passw = sys.argv[2]
    auth_re = HTTPBasicAuth(username, passw)
    r = requests.get("https://api.github.com/user", auth=auth_re)
    print(r.json())
