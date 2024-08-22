#!/usr/bin/node
function factoriel (arg) {
  let result = 1;
  if (isNaN(arg)) {
    console.log(1);
  } else {
    for (let i = arg; i > 0; i--) {
      result *= i;
    }
    console.log(result);
  }
}
const argp = parseInt(process.argv[2]);
factoriel(argp);
