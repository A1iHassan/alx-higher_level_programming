#!/usr/bin/node
const request = require('request');
let i = 0;
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body).results;
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    movies.forEach((element, index) => {
      console.log(element);
      if (element.characters.includes(character)) {
        i += 1;
      }
    });
    console.log(i);
  }
});
