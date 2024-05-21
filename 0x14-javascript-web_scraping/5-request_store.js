#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], data, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
