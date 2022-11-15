#!/usr/bin/node
const text = require('text');

if (process.argv.length > 2) {
  text.readFile(process.argv[2], (err, result) => {
    if (err) {
      console.log(err);
    } else {
      console.log(result.toString('utf-8'));
    }
  });
}