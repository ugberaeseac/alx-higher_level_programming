#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
