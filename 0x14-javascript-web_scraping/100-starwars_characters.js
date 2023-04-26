#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  if (body) {
    const data = JSON.parse(body);
    for (const ch of data.characters) {
      request.get(ch, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
      });
    }
  }
});
