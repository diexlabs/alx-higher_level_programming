#!/usr/bin/python3
'''prints the Header value of a httpResponse'''

import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        h = res.getheader('X-Request-Id')
        print(h)
