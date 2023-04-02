#!/usr/bin/python3
'''list users repos using github api'''

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    endpoint = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    params = {
        'per_page': 10
    }

    res = requests.get(endpoint, headers=headers)
    if res.status_code == 200:
        for commit in res.json()[:10]:
            print(f'{commit["sha"]} {commit["commit"]["author"]["name"]}')
