#!/usr/bin/node
const arg2 = parseInt(process.argv[2]);

if (arg2) {
  console.log('My number: ' + arg2);
} else {
  console.log('Not a number');
}
