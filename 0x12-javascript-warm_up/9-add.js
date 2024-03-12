#!/usr/bin/node
const arg2 = parseInt(process.argv[2]);
const arg3 = parseInt(process.argv[3]);

console.log(add(arg2, arg3));

function add(a, b){
	return(a + b);
}
