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
    registerBtn = $("#registerBtn");
    $("#registerForm").submit( function(e) {
        e.preventDefault();
        registerBtn.removeClass("active");
        afterRegister(registerBtn);
    });
} );
