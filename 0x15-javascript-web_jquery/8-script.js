/* global $ */

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (response) {
  response.results.forEach(function (film) {
    const listItem = $('<li></li>').text(film.title);
    $('#list_movies').append(listItem);
  });
});
