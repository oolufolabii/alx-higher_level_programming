#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    const report = {};

    if (err) {
      console.log(err);
    }
    JSON.parse(body).forEach(element => {
      if (element.completed) {
        if (!report[element.userId]) {
          report[element.userId] = 0;
        }
        report[element.userId]++;
      }
    });
    console.log(report);
  });
}
