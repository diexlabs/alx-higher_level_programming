#!/usr/bin/python3
'''sends a GET request and prints status'''

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url, allow_redirects=True)
    msg = r.text
    print('Body response:')
    print('\t- type:', type(msg))
    print('\t- content:', msg)
