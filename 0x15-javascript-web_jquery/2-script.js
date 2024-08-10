const changeColor = $('header');
$(document).ready(function () {
  $('#red_header').click(function () {
    changeColor.css('color', '#FF0000');
  });
});
