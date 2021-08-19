#!/bin/bash
# Takes an URL,send a GET request to the URL and displays body response
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
