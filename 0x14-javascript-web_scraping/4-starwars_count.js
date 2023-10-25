#!/usr/bin/node

const myProcess = require('process');
const myRequest = require('request');
const argv = myProcess.argv;

if (argv.length === 3) {
  let count = 0;
  const url = argv[2];
  myRequest(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body).results;
      for (const film in films) {
        const characters = films[film].characters;
        for (const character in characters) {
          if (characters[character] === 'https://swapi-api.alx-tools.com/api/people/18/') {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
