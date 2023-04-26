#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, data) {
  if (err) {
    console.log(err);
  }

  response && console.log('code: ' + response.statusCode);
});
