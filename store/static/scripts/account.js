function afterRegister(registerBtn) {
    $.post("/accounts/signup/", $("#registerForm").serialize(), function(data, status) {
        data = JSON.parse(data);

        if (status === "success" && data.success) {
            $("#alertSuccess").removeClass("d-none");
        }
        registerBtn.addClass("active");
    });
}

function afterPasswordRecovery(resetBtn) {

    $.post("/accounts/password_recovery/", $("#resetPasswordForm").serialize(), function(data, status) {
        data = JSON.parse(data);
        if (status === "success" && data.success) {
            $("#alertSuccessReset").removeClass("d-none");
        } else {
            $("#alertFailureReset").removeClass("d-none");
        }

        resetBtn.addClass("active");
    });
}

$().ready( function() {
  // check if password and confirmation password are the same dynamically in change password
  $('#password_change, #confirm_password_change').on('keyup', function (e) {

    if ($('#password_change').val() == $('#confirm_password_change').val()) {

        $(".password_change_Btn").prop("disabled", false);
        $("#message_change").addClass("d-none");
    } else
        $("#message_change").removeClass("d-none");
        

  });

  $('#changePasswordForm').submit(function(e){

    if (!($("#password_change").val() == ""))
      $.post("accounts/reset/<uidb64>/<token>/")
  });

    resetBtn = $("#resetBtn");
    $("#resetPasswordForm").submit( function(e) {
        e.preventDefault();
        resetBtn.removeClass("active");
        afterPasswordRecovery(resetBtn);
    });
} );
