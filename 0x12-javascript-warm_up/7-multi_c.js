#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;
const x = Number(args[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
