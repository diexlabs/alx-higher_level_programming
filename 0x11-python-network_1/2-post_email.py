#!/usr/bin/python3
'''posts an email to a url'''

import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        msg = res.read()
        print(msg.decode('utf8'))
