$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
  $('#remove_item').clik(function () {
    $('ul.my_list li:last-child').remove();
  });
});
