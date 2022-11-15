#!/usr/bin/node
const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (err, result) => {
    if (err) {
      console.log(err);
    } else {
      console.log(result.toString('utf-8'));
    }
  });
}