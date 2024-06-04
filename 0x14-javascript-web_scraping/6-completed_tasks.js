#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const tasksCompleted = {};
  const tasks = JSON.parse(body);
  // Iterate over the tasks and count the completed tasks for each user
  tasks.forEach(task => {
    if (task.completed) {
      const userId = task.userId.toString();
      if (tasksCompleted[userId]) {
        tasksCompleted[userId] += 1;
      } else {
        tasksCompleted[userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
