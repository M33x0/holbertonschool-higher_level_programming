#!/bin/bash
# Send DELETE request to the URL passed as the first arguments and display the body of the responise
curl -s -X DELETE "$1"
