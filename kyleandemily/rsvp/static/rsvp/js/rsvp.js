$(document).ready(function() {

    // form validation/submission for rsvp lookup
    var $lookup_form = $("form#lookup"),
        $first_name = $("#firstname"),
        $last_name = $("#lastname"),
        $container = $("#container");

    $first_name.focus();

    $lookup_form.submit(function (event) {
        event.preventDefault();
        $.ajax({
            url: 'lookup/',
            cache: false,
            data: {
                'first_name': $first_name.val(),
                'last_name': $last_name.val()
            },
            success: function (data, status, jqXHR) {
                $lookup_form.unbind().submit();
                $lookup_form.submit();

            },
            error: function (jqXHR, status) {
                var $error = $('<p>Sorry, we could not find your invitation</p>');
                if($('div#error_msg').is(':empty')) {
                    $($error).appendTo('#error_msg');
                }
            }
        });
    });

    // hide/show functionality for UI
    $(".completeEditButton").hide();

    $(".editButton").click(function(){
      var $occ = $(this).closest('tr').data('value');
      $(".editName" + $occ).toggleClass("viewOnly");
      $('#el').prop('disabled', function(i, v) { return !v; });
      $("#editButton" + $occ).hide();
      $("#completeEdit" + $occ).show();
    });

    $(".completeEditButton").click(function(){
      var $occ = $(this).closest('tr').data('value');
      $(".editName" + $occ).toggleClass("viewOnly");
      $(".editName" + $occ).prop('disabled', function(i, v) { return !v; });
      $("#editButton" + $occ).show();
      $("#completeEdit" + $occ).hide();
    });

    $("#plusOneEdit").hide();

    $("#plusOne").click(function(){
      $('#plusOneEdit').show();
      $('#plusOne').hide();
      $('#addPlusOne').val("1");
    });

    $("#cancelPlusOne").click(function(){
      $('#plusOneEdit').hide();
      $('#plusOne').show();
      $('#addPlusOne').val("0");
    });

    $(".formInputs").focusout(function(){
      var $occ = $(this).closest('tr').data('value');

      var $first = $("#first" + $occ);
          $last = $("#last" + $occ);

      if ($first.val() == '' || $last.val() == '')
        {
            var $error = $('<p id="">This field cannot be blank.</p>');
            if ($('div#error_msg' + $occ).is(':empty')) {
                $($error).appendTo('#error_msg' + $occ);
            }
        }
      else  {
          $('div#error_msg' + $occ).empty();
      }
    });

    $("#plusOneLast").focusout(function(){

      var $plusFirst = $("#plusOneFirst"),
          $plusLast = $("#plusOneLast");

      if ($plusFirst.val() == '' || $plusLast.val() == '')
        {
            var $error = $('<p>Please enter both first and last name to add another guest.</p>');
            if ($('div#plus_one_error_msg').is(':empty')) {
                $($error).appendTo('#plus_one_error_msg');
            }
        }
      else  {
          $('#plus_one_error_msg').empty();
      }
    });
});