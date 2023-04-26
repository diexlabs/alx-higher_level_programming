#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }

  if (body) {
    const data = JSON.parse(body);
    let total = 0;
    for (const film of data.results) {
      if (film.characters.find(ch => ch.endsWith('18/'))) {
        total += 1;
      }
    }
    console.log(total);
  }
});
