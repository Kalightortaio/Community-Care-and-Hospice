$(document).ready(function () {
    $('.content button').click(function () {
        if ( $('.hiddenbox').is('.open') ) {
          $('.buttonindicator').removeClass('fa-minus').addClass('fa-plus');
          $('.hiddenbox').animate({
              height: 'toggle',
              'padding-bottom': 0,
              'padding-top': 0,
          }, 400);
          $('.hiddenbox').removeClass('open');
        } else {
          $('.buttonindicator').removeClass('fa-plus').addClass('fa-minus');
          $('.hiddenbox').animate({
              height: 'toggle',
              'padding-bottom': 5,
              'padding-top': 8,
          }, 400);
          $('.hiddenbox').addClass('open');
        }
    });
});
