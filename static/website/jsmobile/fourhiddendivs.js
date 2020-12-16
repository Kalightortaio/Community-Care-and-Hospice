$(document).ready(function () {
    $('.content .toggle1').click(function () {
        if ( $('.hiddendiv1').is('.open') ) {
          $('.hiddendiv1').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv1').removeClass('open');
        } else {
          $('.hiddendiv1').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv1').addClass('open');
        }
    });
    $('.content .toggle2').click(function () {
        if ( $('.hiddendiv2').is('.open') ) {
          $('.hiddendiv2').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv2').removeClass('open');
        } else {
          $('.hiddendiv2').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv2').addClass('open');
        }
    });
    $('.content .toggle3').click(function () {
        if ( $('.hiddendiv3').is('.open') ) {
          $('.hiddendiv3').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv3').removeClass('open');
        } else {
          $('.hiddendiv3').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv3').addClass('open');
        }
    });
    $('.content .toggle4').click(function () {
        if ( $('.hiddendiv4').is('.open') ) {
          $('.hiddendiv4').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv4').removeClass('open');
        } else {
          $('.hiddendiv4').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv4').addClass('open');
        }
    });
});
