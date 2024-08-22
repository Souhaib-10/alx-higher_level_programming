#!/usr/bin/node
const varg = process.argv[2];
const parseVarg = parseInt(varg);
if (isNaN(parseVarg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseVarg; i++) {
    console.log('C is fun');
  }
}
