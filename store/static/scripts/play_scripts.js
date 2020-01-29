window.addEventListener("message", receiveMessage, false);

function sendMsg(objToSend) {
    window.postMessage(objToSend, "*");
}

function postErrorMessage(infoText) {

    sendMsg({
        messageType: "ERROR",
        info: infoText
    });
}

function postLoad(gameStateAsString) {

    sendMsg({
        messageType: "LOAD", 
        gameState: JSON.parse(gameStateAsString)
    });
}

function receiveMessage(event) {
    
    var data = event.data
    var msgType = ""
    try {
        msgType = data.messageType;
    } catch (error) {
        return; // Just ignore messages without types
    }

    if (msgType == "SCORE") {

    } else if (msgType == "SAVE") {

    } else if (msgType == "LOAD_REQUEST") {


    } else if (msgType == "SETTING") {

    }
}