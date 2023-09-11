#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;
const result = Number(args[2]);
if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + result);
}
