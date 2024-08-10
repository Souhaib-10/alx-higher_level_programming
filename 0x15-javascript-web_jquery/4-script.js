const changeColor = $('header');
$(document).ready(function () {
  $('#toggle_header').click(function () {
    changeColor.toggleClass('red green');
  });
});
