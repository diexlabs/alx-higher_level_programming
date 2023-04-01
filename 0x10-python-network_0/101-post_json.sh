#!/bin/bash
# send a JSON POST request using curl
curl -sL -X POST -H "Content-Type: application/json" --data "@$2" "$1";
