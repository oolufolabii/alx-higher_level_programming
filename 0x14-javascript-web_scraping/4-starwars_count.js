#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(`${process.argv[2]}`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else if (body) {
      const nb = JSON.parse(body).results.filter((elem) => {
        return elem.characters.filter((url) => { return url.includes('18'); }).length;
      }).length;
      console.log(nb);
    }
  });
}
