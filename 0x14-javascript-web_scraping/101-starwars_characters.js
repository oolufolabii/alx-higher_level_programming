#!/usr/bin/node

const request = require('request');
const APL_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${APL_URL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
