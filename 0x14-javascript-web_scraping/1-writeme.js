#!/usr/bin/node

const fs = require('fs');
const myProcess = require('process');
const argv = myProcess.argv;

const path = argv[2];
const content = argv[3];

if (argv.length === 4) {
  fs.writeFile(path, content, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  }
  );
}
