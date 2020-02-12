function onDoProfileUpdate(updateBtn) {

    $.post("/accounts/edit_profile/", $("#updateForm").serialize(), function(data, status) {
        data = JSON.parse(data);
        if (status === "success" && data.success) {
            $("#alertSuccess").removeClass("d-none");
        } else {
            $("#alertFailure").removeClass("d-none");
        }

        updateBtn.addClass("active");
    });
}

$().ready( function() {
    updateBtn = $("#updateProfileButton");
    $("#updateForm").submit( function(e) {
        e.preventDefault();
        updateBtn.removeClass("active");
        onDoProfileUpdate(updateBtn);
    });
} );
