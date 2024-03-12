#!/usr/bin/node
const arg2 = parseInt(process.argv[2]);
if (!isNaN(arg2)) {
  for (let a = 0; a < arg2; a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
