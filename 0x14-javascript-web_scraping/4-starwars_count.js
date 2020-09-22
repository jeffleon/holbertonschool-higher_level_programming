#!/usr/bin/node
const request = require('request');

let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  json.results.forEach((elements) => {
    const character = elements.characters.filter((element) => {
      if (element.endsWith('18/')) { return element; }
    });
    for (const el in character) { if (el !== undefined) { count++; } }
  });
  console.log(count.toString());
});
