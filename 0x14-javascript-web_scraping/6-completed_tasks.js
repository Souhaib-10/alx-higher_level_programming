#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error.message);
  }
  const data = JSON.parse(body);
  const numberValidate = data.reduce((acc, dt) => {
    if (dt.completed === true) {
      acc[dt.userId] = (acc[dt.userId] || 0) + 1;
    }
    return acc;
  }, {});
  console.log(numberValidate);
});
