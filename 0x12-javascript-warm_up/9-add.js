#!/usr/bin/node

function add(a, b) {
	const sum = a + b;
	console.log(sum);
}
const argsChecker1 = Number.parseInt(process.argv[2]);
const argsChecker2 = Number.parseInt(process.argv[3]);


add(argsChecker1, argsChecker2);
