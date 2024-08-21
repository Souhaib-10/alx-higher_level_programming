#!/usr/bin/node
const arg = process.argv[2];
const parseArg = parseInt(arg);
if (isNaN(parseArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseArg}`);
}
