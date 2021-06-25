#!/usr/bin/node
/**
  request GET to swap-api
  return the number of movie for a specific user
  process.argv[2] = the path of the url
**/

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const count = JSON.parse(body).results.filter((elem) => {
      return elem.characters.filter((url) => { return url.includes('18'); }).length;
    }).length;
    console.log(count);
  }
});