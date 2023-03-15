#!/usr/bin/node

const fs = require('fs');

const [first, second, dest] = process.argv.slice(2, 5);

fs.readFile(first, (err, data) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(dest, data, (err) => {
    console.log(err);
  });
});

fs.readFile(second, (err, data) => {
  if (err) {
    console.log(err);
  }

  fs.appendFile(dest, data, (err) => {
    console.log(err);
  });
});
