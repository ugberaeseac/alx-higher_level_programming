$(document).ready(function () {
  function translate () {
    const languageCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;
    $.get(url, function (data, statusText) {
      if (statusText === 'success') {
        $('#hello').text(data.hello);
      }
    });
  }

  $('#btn_translate').click(translate);

  $('#language_code').keydown(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});
