#!/usr/bin/node
const arg = parseInt(process.argv[2]);
let result = 1;
if (isNaN(arg)) {
  console.log(1);
} else {
  for (let i = arg; i > 0; i--) {
    result *= i;
  }
  console.log(result);
}
