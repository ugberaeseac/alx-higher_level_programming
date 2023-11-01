#!/usr/bin/node

const myProcess = require('process');
const myRequest = require('request');
const argv = myProcess.argv;

if (argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
  myRequest(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body);
      for (const i in films.characters) {
        myRequest(films.characters[i], function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}
