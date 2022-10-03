#!/usr/bin/node

const argChecker = Number.parseInt(process.argv[2]);
const word = 'X';

if (Number.isNaN(argChecker) || argChecker === undefined) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < argChecker) {
    console.log(word.repeat(argChecker));
    i++;
  }
}
