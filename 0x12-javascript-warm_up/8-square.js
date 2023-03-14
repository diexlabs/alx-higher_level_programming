#!/usr/bin/node

const number = Number(process.argv[2]);

if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  const size = parseInt(number);
  for (let x = 0; x < size; x++) {
    console.log('X'.repeat(size));
  }
}
