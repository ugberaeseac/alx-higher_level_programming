#!/usr/bin/node

const myRequest = require('request');
const myProcess = require('process');
const argv = myProcess.argv;

if (argv.length === 3) {
  const url = argv[2];
  myRequest(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log('code: ' + response.statusCode);
    }
  }
  );
}
