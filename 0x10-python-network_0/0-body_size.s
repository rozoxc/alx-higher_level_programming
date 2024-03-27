#!/usr/bin/bash

url=$1

# Send a request to the URL and get the size of the response body
size=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size of the response body
echo "$size"

