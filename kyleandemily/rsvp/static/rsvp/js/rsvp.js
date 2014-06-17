$(document).ready(function() {
    var $lookup_form = $("form#lookup"),
        $first_name = $("#firstname"),
        $last_name = $("#lastname"),
        $container = $("#container");

    $first_name.focus();

    $lookup_form.submit(function (event) {
        console.log('first', $first_name.val())
        console.log('last', $last_name.val())
        $.ajax({
            url: '/lookup/',
            cache: false,
            data: {
                'first_name': $first_name.val(),
                'last_name': $last_name.val()
            },
            success: function (data, status, jqXHR) {
                $lookup_form.fadeOut(function () {
                    $container.append(data);
                });
            },
            error: function (jqXHR, status) {
                var $error = $('<div data-alert class="alert-box alert radius">Sorry, we could not find your invitation</div>');
                $lookup_form.append($error);
                $('html, body').animate({
                    scrollTop: $error.offset().top
                }, 500);
            }
        });
        event.preventDefault();
    });
});