#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const nameFile = process.argv[3];
request(url,(error, response, body) => {
    if(error) {
       console.log(error);
     }
    fs.writeFile(nameFile, body, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing to file: ${err.message}`);
    }
});
