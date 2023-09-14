#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;
const firstArg = Number(args[2]);
let result = 0;

function factorial (num) {
  if (isNaN(num) || num === 0 || num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
result = factorial(firstArg);
console.log(result);
