#!/usr/bin/node

const process = require('process');

const argVal = process.argv;
if (argVal[2]) {
  console.log(argVal[2]);
} else {
  console.log('No argument');
}
