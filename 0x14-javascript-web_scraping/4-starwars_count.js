#!/usr/bin/node
const request = require('request');

let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  json.results.forEach((elements) => {
    var character = elements.characters.filter((element) => {
      const index = element.search('people/');
      const split = element.slice(index + 7).replace('/', '');
      if (parseInt(split, 10) === 18) { return split; }
    });
    for (const el in character) { if (el) { count++; } }
  });
  console.log(count);
});
