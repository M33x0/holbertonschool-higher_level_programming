#!/usr/bin/node

const number = parseInt(process.arv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
