#!/usr/bin/node

const fs = require('fs');
const myProcess = require('process');
const argv = myProcess.argv;

if (argv.length === 3) {
  fs.readFile(argv[2], 'utf-8', function (err, file) {
    if (err) {
      console.log(err);
    } else {
      console.log(file.toString());
    }
  }
  );
}
