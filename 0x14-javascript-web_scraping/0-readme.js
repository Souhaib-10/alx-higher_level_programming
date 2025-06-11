#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const path = process.argv[2];

fs.readFile(path, 'utf8', (err, data) => {
  console.log(data || err);
});
