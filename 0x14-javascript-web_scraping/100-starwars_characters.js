#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films', (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  const episode = json.results.filter((element) => parseInt(element.episode_id) === parseInt(process.argv[2]));
  episode[0].characters.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) { console.log(error); }
      const json = JSON.parse(body);
      console.log(json.name);
    });
  });
});
