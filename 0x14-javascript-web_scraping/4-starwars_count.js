#!/usr/bin/node
const request = require("request");
const process = require("process");
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach((film) => {
    const filmChar = film.characters;
    filmChar.map((fr) => {
      if (fr.includes("18")) {
        count++;
      }
    });
  });
  console.log(count);
});

