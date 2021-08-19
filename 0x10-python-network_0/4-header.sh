#!/bin/bash
# Take anURL as an arguments,send a GET request to the URL and display the body of the response
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"