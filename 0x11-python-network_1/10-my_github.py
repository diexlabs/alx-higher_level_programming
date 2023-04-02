#!/usr/bin/python3
'''display Github password using api'''

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    endpoint = 'https://api.github.com/user'

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {password}',
        'X-Github-Api-Version': '2022-11-28'
    }

    res = requests.get(endpoint, headers=headers)
    if res.status_code == 200:
        res_json = res.json()
        print(res_json['id'])
