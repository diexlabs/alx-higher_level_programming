#!/usr/bin/python3
'''catches http Error'''

import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.getcode())
