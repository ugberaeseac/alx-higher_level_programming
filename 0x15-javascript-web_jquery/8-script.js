$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data, statusText) {
    if (statusText === 'success') {
      const films = data.results;
      for (const title in films.title) {
        $('#list_movies').append('<li>' + films[title] + '</li>');
      }
    }
  });
});
