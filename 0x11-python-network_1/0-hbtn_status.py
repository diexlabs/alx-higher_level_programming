#!/usr/bin/python3
'''opens a webpage using urllib and prints content'''

import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as res:
        msg = res.read()
        print('Body response:')
        print('\t- type:', type(msg))
        print('\t- content:', msg)
        print('\t- utf8 content:', msg.decode('utf8'))
