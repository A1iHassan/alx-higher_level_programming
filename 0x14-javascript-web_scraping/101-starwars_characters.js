#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(`${url}${process.argv[2]}`, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(data).characters;
    characters.forEach((element, index) => {
      request(element, (err2, res2, data2) => {
        if (err2) {
          console.log(err2);
        } else {
          console.log(JSON.parse(data2).name);
        }
      });
    });
  }
});
