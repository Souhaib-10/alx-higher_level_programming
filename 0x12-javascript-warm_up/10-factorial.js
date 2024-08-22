#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1; // Factorial of 0 or NaN is 1
  } else {
    return n * factorial(n - 1); // Recursive call
  }
}

const num = parseInt(process.argv[2]);
const result = factorial(num);
console.log(result);
