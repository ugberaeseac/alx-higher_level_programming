#!/usr/bin/node
const myProcess = require('process');
const args = myProcess.argv;
let sum = 0;

function add (a, b) {
  sum = Number(a) + Number(b);
  console.log(sum);
}
add(args[2], args[3]);
