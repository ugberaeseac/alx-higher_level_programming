#!/usr/bin/node

const process = require('process');
const args = process.argv;
const argsLength = args.length;
if (argsLength <= 2) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
