#!/usr/bin/node
const countArg = process.argv.length;
if (countArg > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
