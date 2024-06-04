#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printAllCharacters(characters, 0);
  }
});

function printAllCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printAllCharacters(characters, index + 1);
      }
    }
  });
}
