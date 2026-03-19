#!/usr/bin/node

function factorial (n) {
  const number = parseInt(n);
  if (isNaN(number) || num <= 1) return 1;
  return number * factorial(number - 1);
}

const n = process.argv[2];
console.log(factorial(n));
