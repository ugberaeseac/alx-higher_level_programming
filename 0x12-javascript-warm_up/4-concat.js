#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;

console.log(args[2] + ' is ' + args[3]);
