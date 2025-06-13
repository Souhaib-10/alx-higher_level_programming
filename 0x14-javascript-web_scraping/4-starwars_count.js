#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film in films) {
    const filmChar = films[film].characters;
    for (const fr in filmChar) {
      if (filmChar[fr].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
