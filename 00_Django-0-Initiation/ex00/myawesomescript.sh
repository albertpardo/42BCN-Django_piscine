#!/bin/bash

# Check if a URL is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <bit.ly link>"
  exit 1
fi

# Use curl to get the headers, grep to find the location and cut to select the URL
curl -I "$1" 2>/dev/null | grep 'Location' | cut -d ' ' -f2
