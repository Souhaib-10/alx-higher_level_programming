#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
