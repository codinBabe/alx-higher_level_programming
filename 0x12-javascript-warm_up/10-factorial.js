#!/usr/bin/node
const arg2 = parseInt(process.argv[2]);

console.log(factorial(arg2));

function factorial (x) {
  if (isNaN(x) || x === 1) {
    return 1;
  }

  return (x * factorial(x - 1));
}
