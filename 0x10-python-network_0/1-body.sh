#!/bin/bash
# sends out a GET request and displays the response body if status OK
curl -sL -X GET "$1";
