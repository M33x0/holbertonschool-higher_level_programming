#!/usr/bin/node
let fs = require('fs');
let args = process.argv;
let file1 = fs.readFileSync(args[2], 'utf8');
let file2 = fs.readFileSync(args[3], 'utf8');
let data = file1 + file2;
fs.writeFile(args[4], data, err => {
  if (err) {
    console.error(err);
  }
});