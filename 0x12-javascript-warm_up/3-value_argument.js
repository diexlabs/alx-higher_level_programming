#!/usr/bin/node

const first = process.argv[2];

if (!first) {
  console.log('No argument');
} else {
  console.log(first);
}
