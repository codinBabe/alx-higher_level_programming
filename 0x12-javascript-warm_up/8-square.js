#!/usr/bin/node
const arg2 = parseInt(process.argv[2]);
if (!isNaN(arg2)) {
  if (arg2 > 0) {
    for (let a = 0; a < arg2; a++) {
      let row = '';
      for (let b = 0; b < arg2; b++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
