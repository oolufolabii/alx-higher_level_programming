#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', (err, result) => { if (err) console.log(err); });
  } catch (err) {
    console.log(err);
  }
});
