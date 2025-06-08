#!/usr/bin/python3
''' A script that take in a URL and an email send a Post request
    and finally display of the body of the response
'''

import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.post(url, data={'email': sys.argv[2]})
    print(req.text)
