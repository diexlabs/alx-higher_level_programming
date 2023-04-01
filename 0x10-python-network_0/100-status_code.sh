#!/bin/bash
# outputs the status code of a request
curl -sL -o /dev/null -w "%{http_code}" "$1"
