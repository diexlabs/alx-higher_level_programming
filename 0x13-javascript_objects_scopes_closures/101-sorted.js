#!/usr/bin/node

const dict = require('./101-data').dict;

const trDict = {};

Object.entries(dict).forEach((value, index, arr) => {
  if (value[1] in trDict) {
    trDict[value[1]].push(value[0]);
  } else {
    trDict[value[1]] = [];
    trDict[value[1]].push(value[0]);
  }
});

console.log(trDict);
