#!/usr/bin/python3
''' A python script that take a URL and display X-Request-Id value'''

import sys
from urllib.request import Request, urlopen


url = sys.argv[1]
req = Request(url)
with urlopen(req) as response:
    res_format = response.read().decode('utf-8')
    print(response.headers.get('X-Request-Id'))
