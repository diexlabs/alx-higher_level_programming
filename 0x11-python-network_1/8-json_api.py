#!/usr/bin/python3
'''a search api with reqeusts package'''

import sys
import requests


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""

    params = {'q': q}
    res = requests.get(url, params=params, allow_redirects=True)

    try:
        j = res.json()
        if not j:
            print("No result")
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except ValueError:
        print("Not a valid JSON")
