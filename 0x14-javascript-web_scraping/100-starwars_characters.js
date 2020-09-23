#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  json.characters.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) { console.log(error); }
      const json = JSON.parse(body);
      console.log(json.name);
    });
  });
});
