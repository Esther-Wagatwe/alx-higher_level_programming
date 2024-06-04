#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntillesId = 18;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    const moviesWithWedgeAntilles = movies.filter(movie =>
      movie.characters.some(charUrl => charUrl.includes(`/${wedgeAntillesId}/`))
    );
    console.log(moviesWithWedgeAntilles.length);
  }
});
