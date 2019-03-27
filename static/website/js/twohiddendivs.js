$(document).ready(function () {
    $('.content .toggle1').click(function () {
        if ( $('.hiddendiv1').is('.open') ) {
          $('.toggle1 span').html('show more&nbsp;&nbsp;<i class="fas fa-caret-down fa-lg"></i>');
          $('.hiddendiv1 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv1').removeClass('open');
        } else {
          $('.toggle1 span').html('show less&nbsp;&nbsp;<i class="fas fa-caret-up fa-lg"></i>');
          $('.hiddendiv1 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv1').addClass('open');
        }
    });
    $('.content .toggle2').click(function () {
        if ( $('.hiddendiv2').is('.open') ) {
          $('.toggle2 span').html('show more&nbsp;&nbsp;<i class="fas fa-caret-down fa-lg"></i>');
          $('.hiddendiv2 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv2').removeClass('open');
        } else {
          $('.toggle2 span').html('show less&nbsp;&nbsp;<i class="fas fa-caret-up fa-lg"></i>');
          $('.hiddendiv2 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv2').addClass('open');
        }
    });
});
