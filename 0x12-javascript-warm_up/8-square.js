#!/usr/bin/node

const myProcess = require('process');
const args = myProcess.argv;
const firstArgs = Number(args[2]);

if (isNaN(firstArgs)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgs; i++) {
    console.log('X'.repeat(firstArgs));
  }
}
