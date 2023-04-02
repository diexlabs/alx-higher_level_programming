#!/usr/bin/python3
'''posts an email to a url'''

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    res = requests.post(url, data=data)

    print(res.text)
