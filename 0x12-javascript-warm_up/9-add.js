#!/usr/bin/node

const first = Number(process.argv[2]);
const second = Number(process.argv[3]);

function add (x, y) {
  return x + y;
}

console.log(add(first, second));
