
#!/usr/bin/python3
"""Fetches a URL."""
import requests


if __name__ == '__main__':
	html_response = requests.get('https://intranet.hbtn.io/status')
	print('Body response:')
	print('\t- type: {}'.format(type(html_response.text)))
	print('\t- content: {}'.format(html_response.text))
