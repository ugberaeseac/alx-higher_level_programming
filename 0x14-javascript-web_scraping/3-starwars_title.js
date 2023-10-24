#!/usr/bin/node

const myProcess = require('process');
const myRequest = require('request');
const argv = myProcess.argv;

if (argv.length === 3) {
  const id = argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

  myRequest(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
