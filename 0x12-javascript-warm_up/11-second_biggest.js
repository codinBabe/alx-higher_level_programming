#!/usr/bin/node

const args = process.argv.slice(2);
const arr = [];

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (const a of args) {
    arr.push(parseInt(a));
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
