#!/usr/bin/python3
'''prints a header from response'''

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url, allow_redirects=True)
    h = r.headers.get('X-Request-Id')
    print(h)
