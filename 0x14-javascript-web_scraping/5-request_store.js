#!/usr/bin/node

const myProcess = require('process');
const fs = require('fs');
const myRequest = require('request');
const argv = myProcess.argv;

if (argv.length === 4) {
  const path = argv[3];
  const url = argv[2];
  myRequest(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(path, body, 'utf-8', function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
