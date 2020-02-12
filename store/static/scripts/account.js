function afterRegister(registerBtn) {
    $.post("/accounts/signup/", $("#registerForm").serialize(), function(data, status) {
        data = JSON.parse(data);

        if (status === "success" && data.success) {
            $("#alertSuccess").removeClass("d-none");
        }
        registerBtn.addClass("active");
    });
}

$().ready( function() {

    registerBtn = $(".registerBtn");
    $(".registerForm").submit( function(e) {
        e.preventDefault();
        registerBtn.removeClass("active");
        afterRegister(registerBtn);
    });
} );

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
    resetBtn = $("#resetBtn");
    $("#resetPasswordForm").submit( function(e) {
        e.preventDefault();
        resetBtn.removeClass("active");
        afterPasswordRecovery(resetBtn);
    });
} );
