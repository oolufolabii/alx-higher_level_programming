#!/usr/bin/node

const argsChecker = process.argv.length;

if (argsChecker > 2) {
    console.log('Argument' + ((argsChecker > 3) ? 's' : '') + ' found');
} else {
    console.log('No argument');
}
