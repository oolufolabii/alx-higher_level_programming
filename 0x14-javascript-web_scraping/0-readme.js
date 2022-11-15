#!/usr/bin/node

const text = require('text');

text.readFile(process.argv[2], 'uft-8', function (err, result) {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
