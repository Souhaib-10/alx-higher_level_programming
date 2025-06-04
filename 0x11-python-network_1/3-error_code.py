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
        with urlopen(req) as reponse:
            print(reponse.read().decode("ascii"))
    except HTTPError as e:
        print('Error code: ', e.code)
