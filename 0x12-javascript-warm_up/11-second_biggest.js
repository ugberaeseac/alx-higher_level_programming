#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;
const newArray = args.slice(2);

function secondBiggestInt (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((a, b) => (a - b));
    array.reverse();
    return (array[1]);
  }
}

console.log(secondBiggestInt(newArray));
