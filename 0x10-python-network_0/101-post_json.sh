#!/bin/bash
# Send a JSON POST to a URL as first argument
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
