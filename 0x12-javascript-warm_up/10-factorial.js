#!/usr/bin/node

function factorial (n) {
  if (n <= 1 || Number.isNaN(n)) {
    return 1;
  }

  return n * factorial(n - 1);
}

const number = Number(process.argv[2]);
console.log(factorial(number));
