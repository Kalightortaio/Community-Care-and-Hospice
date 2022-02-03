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
});
