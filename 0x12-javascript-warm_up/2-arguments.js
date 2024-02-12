#!/usr/bin/node

const val = process.argv.length - 2;
if (val === 0) {
  console.log('No argument');
} else if (val === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
