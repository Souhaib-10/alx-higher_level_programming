#!/usr/bin/python3
''' A script that take in a URL and an email send a Post request
    and finally display of the body of the response
'''

import sys
from urllib.request import Request, urlopen
import urllib.parse

url = sys.argv[1]
value = {'email' : sys.argv[2]}
data = urllib.parse.urlencode(value)
data = data.encode('ascii')
req = Request(url, data)
with urlopen(req) as res:
    print(res.read().decode('utf-8'))
