#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }

  if (body) {
    const data = JSON.parse(body);
    const dataJson = {};
    for (const item of data) {
      if (item.completed) {
        if (item.userId in dataJson) {
          dataJson[item.userId] += 1;
        } else {
          dataJson[item.userId] = 1;
        }
      }
    }
    console.log(dataJson);
  }
});
