$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;
    $.get(url, function (data, statusText) {
      if (statusText === 'success') {
        $('#hello').text(data.hello);
      }
    });
  });
});
