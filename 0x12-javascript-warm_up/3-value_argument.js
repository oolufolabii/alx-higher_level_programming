#!/usr/bin/node

const argsChecker = process.argv[2];

if (argsChecker === undefined) {
    console.log('No argument');
} else {
    console.log(argsChecker);
}
