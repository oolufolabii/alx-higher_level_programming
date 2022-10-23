
#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable"""

if __name__ == "__main__":
	import urllib.request
	import sys

	with urllib.request.urlopen(sys.argv[1]) as response:
		head_request = response.headers.get('X-Request-Id')
		print(head_request)
