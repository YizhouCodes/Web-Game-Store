$(document).ready(function() {
    window.addEventListener("message", receiveMessage, false);

    var value = getCookie('csrftoken');
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", value);
            }
        }
    });
});

function sendMsg(objToSend) {

    document.getElementById("game").contentWindow.postMessage(objToSend, "*");
}

function postErrorMessage(infoText) {

    sendMsg({
        messageType: "ERROR",
        info: infoText
    });
}

function postLoad(gameStateAsObj) {

    sendMsg({
        messageType: "LOAD", 
        gameState: gameStateAsObj
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function receiveMessage(event) {
    
    var data = event.data
    var msgType = ""
    try {
        msgType = data.messageType;
    } catch (error) {
        return; // Just ignore messages without types
    }

    reqUrl = window.location.href.split('?')[0];

    if (msgType == "SCORE") {
        reqUrl += "/post_score";

        $.post(reqUrl, {score: data.score}, function(data, status) {
            data = JSON.parse(data);
            if (status !== "success") {
                postErrorMessage("Cannot save score: cannot send post");
            } else if (!data["status"]) {
                postErrorMessage("Cannot save score: " + data["info"]);
            }
        });

    } else if (msgType == "SAVE") {
        reqUrl += "/save_state"
        
        $.post(reqUrl, JSON.stringify(data.gameState), function(data, status) {
            data = JSON.parse(data);

            if (status !== "success") {
                postErrorMessage("Cannot save state: cannot send post");
            } else if (!data["status"]) {
                postErrorMessage("Cannot save state: " + data["info"]);
            }
        });
    } else if (msgType == "LOAD_REQUEST") {
        reqUrl += "/get_state"
        
        $.get(reqUrl, JSON.stringify(data.gameState), function(data, status) {
            data = JSON.parse(data);
            
            if (status !== "success") {
                postErrorMessage("Cannot load: cannot send post");
            } else if (!data["status"]) {
                postErrorMessage("Cannot load: " + data["info"]);
            } else {
                postLoad(data.gameState);
            }
        });
    } else if (msgType == "SETTING") {
        reqUrl += "/post_settings"

        $.post(reqUrl, JSON.stringify(data.options), function(data, status) {
            data = JSON.parse(data);
            if (status !== "success") {
                postErrorMessage("Cannot save settings: cannot send post");
            } else if (!data["status"]) {
                postErrorMessage("Cannot save settings: " + data["info"]);
            }
        });

        try {
            $("#game").attr("style", "width: " + data.options.width + "px;height: " + data.options.height + "px")
        } catch (error) {
            ; // Just skip this, options don't have width and/or hight fields
        }
    }
}