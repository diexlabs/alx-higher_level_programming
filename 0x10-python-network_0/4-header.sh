#!/bin/bash
# sends a GET request with custom header
curl -sL -X GET -H "X-School-User-Id: 98" "$1";
