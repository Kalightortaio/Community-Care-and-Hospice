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
    $('.content .toggle3').click(function () {
        if ( $('.hiddendiv3').is('.open') ) {
          $('.toggle3 span').html('show more&nbsp;&nbsp;<i class="fas fa-caret-down fa-lg"></i>');
          $('.hiddendiv3 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv3').removeClass('open');
        } else {
          $('.toggle3 span').html('show less&nbsp;&nbsp;<i class="fas fa-caret-up fa-lg"></i>');
          $('.hiddendiv3 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv3').addClass('open');
        }
    });
    $('.content .toggle4').click(function () {
        if ( $('.hiddendiv4').is('.open') ) {
          $('.toggle4 span').html('show more&nbsp;&nbsp;<i class="fas fa-caret-down fa-lg"></i>');
          $('.hiddendiv4 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv4').removeClass('open');
        } else {
          $('.toggle4 span').html('show less&nbsp;&nbsp;<i class="fas fa-caret-up fa-lg"></i>');
          $('.hiddendiv4 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv4').addClass('open');
        }
    });
    $('.content .toggle5').click(function () {
        if ( $('.hiddendiv5').is('.open') ) {
          $('.toggle5 span').html('show more&nbsp;&nbsp;<i class="fas fa-caret-down fa-lg"></i>');
          $('.hiddendiv5 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv5').removeClass('open');
        } else {
          $('.toggle5 span').html('show less&nbsp;&nbsp;<i class="fas fa-caret-up fa-lg"></i>');
          $('.hiddendiv5 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv5').addClass('open');
        }
    });
    $('.content .toggle6').click(function () {
        if ( $('.hiddendiv6').is('.open') ) {
          $('.toggle6 span').html('show more&nbsp;&nbsp;<i class="fas fa-caret-down fa-lg"></i>');
          $('.hiddendiv6 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv6').removeClass('open');
        } else {
          $('.toggle6 span').html('show less&nbsp;&nbsp;<i class="fas fa-caret-up fa-lg"></i>');
          $('.hiddendiv6 div').animate({
              height: 'toggle',
          }, 400);
          $('.hiddendiv6').addClass('open');
        }
    });
});
