#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${episode}`, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  body && console.log(JSON.parse(body).title);
});
