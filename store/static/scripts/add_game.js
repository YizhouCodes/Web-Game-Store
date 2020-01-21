function addGame(addingBtn) {
    
    $.post("/games/add/", $("#addingForm").serialize(), function(data, status) {
        data = JSON.parse(data);

        if (status === "success" && data.success) {
            
            // Redirect to home
            document.location.href = '/'
        } else {
            
            $("#alertFailure").removeClass("d-none");
        }

        addingBtn.addClass("active");
    });
}

$().ready( function() {
    addingBtn = $("#addingGameButton");
    $("#addingForm").submit( function(e) {
        e.preventDefault();
        addingBtn.removeClass("active");
        addGame(addingBtn)
    });
});