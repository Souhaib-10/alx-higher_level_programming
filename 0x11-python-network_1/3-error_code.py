#!/usr/bin/python3
'''Python script that takes in a URL,
    sends a request to the URL and displays the body of the response
'''

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        if hasattr(e, 'code'):
            print('Error code: {}'.format(e.code))
