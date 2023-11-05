$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data, statusText) {
    if (statusText === 'success') {
      $('#character').text(data.name);
    }
  });
});
