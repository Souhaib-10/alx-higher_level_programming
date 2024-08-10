const changeColor = $('header');
$(document).ready(function () {
  $('#red_header').click(function () {
    changeColor.addClass('red');
  });
});
