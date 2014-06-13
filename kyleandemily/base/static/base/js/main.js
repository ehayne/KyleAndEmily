$(document).ready(function() {
	$(".fancybox").fancybox();

    $(".fancybox").fancybox({
		'openEffect'	:	'elastic',
		'closeEffect'	:	'elastic',
	});

    //Change title position; show overlay after content has loaded
  $(".fancybox").fancybox({
    helpers:  {
        title : {
            type : 'outside'
        },
        overlay : {
            showEarly : false
        }
    }
  });
});