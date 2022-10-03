#!/usr/bin/node

const argsChecker = Number.parseInt(process.argv[2]);

if (Number.isNaN(argsChecker)) {
  console.log('Not a number')
} else {
  console.log('My number: ' + argsChecker)
}
