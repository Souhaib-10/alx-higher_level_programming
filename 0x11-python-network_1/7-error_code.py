#!/usr/bin/python3
'''Python script that takes in a URL,
    sends a request to the URL and displays the body of the response
    display errors
'''

if __name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])
    try:
        print(req.text)
    except raise_for_status() as e:
        if e.status_code >= 400:
            print("Error code: {}".format(e.code))
