#!/usr/bin/node

/**
* request GET url and print status
* process.argv[2] = path of the url to request
*/

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } console.log('code:', response.statusCode);
});
