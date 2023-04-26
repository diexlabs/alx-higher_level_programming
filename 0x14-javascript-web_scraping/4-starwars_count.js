#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }

  if (body) {
    const data = JSON.parse(body);
    let total = 0;
    for (const film of data.results) {
      if (film.characters.includes(character)) {
        total += 1;
      }
    }
    console.log(total);
  }
});
