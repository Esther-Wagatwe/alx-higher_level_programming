#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const tasks = JSON.parse(body);
  const tasksCompleted = {};
  // Iterate over the tasks and count the completed tasks for each user
  tasks.forEach((task) => {
    if (task.completed) {
      if (tasksCompleted[task.userId]) {
        tasksCompleted[task.userId] += 1;
      } else {
        tasksCompleted[task.userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
