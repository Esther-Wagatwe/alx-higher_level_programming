#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const tasksCompleted = {};
    tasks.forEach((task) => {
      if (task.completed && tasksCompleted[task.userId] === undefined) {
        tasksCompleted[task.userId] = 1;
      } else if (task.completed) {
        tasksCompleted[task.userId] += 1;
      }
    });
    console.log(tasksCompleted);
  }
});
