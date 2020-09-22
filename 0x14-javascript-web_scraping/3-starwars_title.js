#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2].toString(), (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  console.log(json.title);
});
