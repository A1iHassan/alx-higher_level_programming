#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

function search (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(data).name);
      }
    });
  });
}

request(`${url}${process.argv[2]}`, async (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(data).characters;
    const promises = characters.map((character) => search(character));
    const names = await Promise.all(promises);
    for (const name of names) {
      console.log(name);
    }
  }
});
