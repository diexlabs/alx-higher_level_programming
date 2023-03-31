#!/bin/bash
# querys the server for allowed method using curl
curl -sL -X OPTIONS --head "$1" | grep 'Allow:' | cut -d' ' -f2-;
