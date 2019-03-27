var tts = false;
window.speechSynthesis.cancel();
$(document).ready(function () {
    //Detects if zoomed
    var hasZoomed = localStorage['testforzoom']
    if (!hasZoomed) {
        var zoom = 1;
        localStorage['zoom'] = zoom;
    } else {
        var zoom = localStorage['zoom']
        $('body').attr('style','zoom:'+ zoom +';-moz-transform:scale('+ zoom +');-moz-transform-origin: 0 0');
    }
    //Sticky Navigation
    var totalH = $('#stickyNav').offset().top;
    $(window).bind('scroll', function () {
        var vPos = $(window).scrollTop();

        if (totalH + 263 < vPos) {
            $('#stickyNav').css({
                'position': 'fixed',
                'height': '70px',
                'top': '0'
            })
            $('.utility-header').css({
                'height': '30px'
            })
            $('.mid-header').css({
                'display': 'none'
            })
            $('.main-header').css({
                'height': '40px'
            })
            $('.utility-list-items').css({
                'padding-top': '1px',
                'padding-bottom': '1px'
            })
            $('.tts').css({
                'padding-top': '1px',
                'padding-bottom': '1px'
            })
            $('.phone-wrapper').css({
                'padding-top': '1px',
                'padding-bottom': '1px'
            })
            $('.main-list-items').css({
                'padding-top': '10px',
                'padding-bottom': '9px'
            })
            $('.searchbar').css({
                'padding-top': '4px',
                'padding-bottom': '4px'
            })
            $('.searchbar input').css({
                'height': '28px'
            })
            $('.searchbar button').css({
                'height': '28px'
            })
            $('.dropdown-content').css({
                'margin-top': '8px'
            })
        } else {
            $('#stickyNav').css({
                'position': 'absolute',
                'height': '238px',
                'top': ''
            })
            $('.utility-header').css({
                'height': '54px'
            })
            $('.mid-header').css({
                'display': 'block'
            })
            $('.main-header').css({
                'height': '60px'
            })
            $('.utility-list-items').css({
                'padding-top': '13px',
                'padding-bottom': '13px'
            })
            $('.tts').css({
                'padding-top': '13px',
                'padding-bottom': '13px'
            })
            $('.phone-wrapper').css({
                'padding-top': '13px',
                'padding-bottom': '13px'
            })
            $('.main-list-items').css({
                'padding-top': '20px',
                'padding-bottom': '20px'
            })
            $('.searchbar').css({
                'padding-top': '8px',
                'padding-bottom': '8px'
            })
            $('.searchbar input').css({
                'height': '40px'
            })
            $('.searchbar button').css({
                'height': '40px'
            })
            $('.dropdown-content').css({
                'margin-top': '20px'
            })
        }
    });
    //Text to Speech
    function speak(message) {
        var msg = new SpeechSynthesisUtterance(message)
        var voices = window.speechSynthesis.getVoices()
        msg.voice = voices[0]
        window.speechSynthesis.speak(msg)
    }
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    $('.tts').click(function () {
          $('.toggleUtil').attr('style','display:inline-block !important');
          $('.tts').attr('style','display:none !important');
          tts = true;
    });
    $('.toggleUtil').click(function () {
          $('.tts').attr('style','display:inline-block !important');
          $('.toggleUtil').attr('style','display:none !important');
          tts = false;
    });
    $('span').on( "mouseover", async function () {
          await sleep(500);
          if (($(this).is(':hover')) === false) {
            return;
          }
          if (tts == true) {
              window.speechSynthesis.cancel();
              await sleep(500);
              var message = $(this).text();
              speak(message);
          } else {
              return;
          }
    });
    //Zoom Functions
    $('.zoomout').click(function () {
          zoom = 0.75;
          localStorage['zoom'] = zoom;
          localStorage['testforzoom'] = true;
          $('body').attr('style','zoom:'+ zoom +';-moz-transform:scale('+ zoom +');-moz-transform-origin: 0 0');
    });
    $('.zoomreset').click(function () {
          zoom = 1;
          localStorage['zoom'] = zoom;
          localStorage['testforzoom'] = false;
          $('body').attr('style','zoom:'+ zoom +';-moz-transform:scale('+ zoom +');-moz-transform-origin: 0 0');
    });
    $('.zoomin').click(function () {
          zoom = 1.4;
          localStorage['zoom'] = zoom;
          localStorage['testforzoom'] = true;
          $('body').attr('style','zoom:'+ zoom +';-moz-transform:scale('+ zoom +');-moz-transform-origin: 0 0');
    });
});
