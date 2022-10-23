#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":

    import urllib.request as request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        if response.readable():
            html_request = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(html_request)))
            print("\t- content: {}".format(html_request))
            print("\t- utf8 content: {}".format(html_request.decode("utf-8")))
