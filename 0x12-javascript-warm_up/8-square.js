#!/usr/bin/node
const arg = process.argv[2];
const parseArg = parseInt(arg);
if (isNaN(parseArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseArg; i++) {
    let numberx = '';
    for (let j = 0; j < parseArg; j++) {
      numberx += 'X';
    }
    console.log(numberx);
  }
}
