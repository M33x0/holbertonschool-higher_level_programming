#!/usr/bin/node

function factorial (number) {
  if (number < 0) {
    return (-1);
  } else if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

const args1 = parseInt(process.argv[2]);
if (isNaN(args1)) {
  console.log(1);
} else {
  console.log(factorial(args1));
}
