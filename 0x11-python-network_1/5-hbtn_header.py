#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""


if __name__ == "__main__":
    import requests
    import sys

    data = requests.get(sys.argv[1])
    print(data.headers.get('X-Request-Id'))
