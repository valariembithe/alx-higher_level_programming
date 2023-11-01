#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/';
const movie_id = process.argv[2]

request(URL + movie_id, function(err, response, body) {
  if (err) {
    console.log(err);
    } else if (response.statusCode === 200) {
      const responseJson = JSON.parse(body);
      console.log(responseJson.title);
    } else {
      console.log('Error code: ' + response.statusCode);
    }
});
