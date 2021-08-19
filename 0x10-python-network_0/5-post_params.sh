#!/bin/bash
# Take a URL ,send a POST request to the passed to the  URL,and displays the body of the response
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

