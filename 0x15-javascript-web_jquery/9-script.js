$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data, statusText) {
    if (statusText === 'success') {
      $('#hello').text(data.hello);
    }
  });
});
