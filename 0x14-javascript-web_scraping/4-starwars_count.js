#!/usr/bin/node
const request = require('request');
let i = 0;
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body).results;
    movies.forEach((element, index) => {
      element.characters.forEach((el, ind) => {
        if (el.includes('/18/')) {
          i += 1;
        }
      });
    });
    console.log(i);
  }
});
