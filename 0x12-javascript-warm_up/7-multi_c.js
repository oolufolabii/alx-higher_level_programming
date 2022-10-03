#!/usr/bin/node
const argChecker = Number.parseInt(process.argv[2]);
const sentence = 'C is fun';

if (Number.isNaN(argChecker) || argChecker === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < argChecker){
    console.log(sentence);
    i++;
  }  
}
