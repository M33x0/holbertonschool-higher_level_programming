#!/usr/bin/node
const size = parseInt(process.argv[2]);
let value = '';
if (process.argv[2] === 0 || isNaN(process.argv[2])) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    value += 'X';
  }
  console.log(value);
  value = '';
}
