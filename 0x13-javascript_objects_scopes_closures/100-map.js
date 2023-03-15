#!/usr/bin/node

const arr = require('./100-data').list;

const arr2 = arr.map((val, index) => val * index);
console.log(arr);
console.log(arr2);
