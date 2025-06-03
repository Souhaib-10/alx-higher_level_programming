#!/usr/bin/python3
''' Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the X-Request-Id variable
    found in the header of the response.
'''
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys


    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers["X-Request-Id"])
