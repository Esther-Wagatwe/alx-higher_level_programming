/* global $ */

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
    $.getJSON(url, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
