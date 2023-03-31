#!/bin/bash
# curls a url and prints out the content size
curl -s "$1" | wc -c;
