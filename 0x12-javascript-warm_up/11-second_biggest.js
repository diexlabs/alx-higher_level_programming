#!/usr/bin/node

let a = process.argv.slice(2);

if (a.length <= 1) {
  console.log(0);
} else {
  a = a.map((n) => Number(n));
  a.sort((a, b) => a - b);
  const second = a[a.length - 2];
  console.log(second);
}
