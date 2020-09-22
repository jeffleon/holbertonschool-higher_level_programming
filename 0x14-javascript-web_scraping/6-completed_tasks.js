#!/usr/bin/node
const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  const tasks = {};
  json.forEach((element) => {
    if (element.completed) {
      if (!(element.userId in tasks)) {
        tasks[`${element.userId}`] = 1;
      } else {
        tasks[`${element.userId}`] += 1;
      }
    }
  });
  console.log(tasks);
});
