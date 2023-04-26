#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request
  .get(url)
  .on('error', function (err) {
    console.log(err);
  })
  .pipe(fs.createWriteStream(filename));
