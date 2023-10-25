#!/usr/bin/node

const myProcess = require('process');
const myRequest = require('request');
const argv = myProcess.argv;
const url = argv[2];

if (argv.length === 3) {
  const myDict = {};
  myRequest(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const tasks = JSON.parse(body);
      for (let i = 0; i < tasks.length; i++) {
        if (tasks[i].completed === true) {
          if (myDict[tasks[i].userId] === undefined) {
            myDict[tasks[i].userId] = 1;
          } else {
            myDict[tasks[i].userId] += 1;
          }
        }
      }
    }
    console.log(myDict);
  });
}
