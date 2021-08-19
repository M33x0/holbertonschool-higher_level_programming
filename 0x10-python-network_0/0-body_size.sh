#!/bin/bash
# Take a URL,sends a request to that URL and displays body size
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
