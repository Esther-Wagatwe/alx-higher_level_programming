/* global $ */

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.getJSON(url, function (response) {
  $('#hello').text(response.hello);
});
