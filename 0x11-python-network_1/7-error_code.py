#!/usr/bin/python3
'''catches http Error'''

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    res = requests.get(url, allow_redirects=True)
    status = res.status_code
    if status >= 400:
        print('Error code:', status)
    else:
        print(res.text)
