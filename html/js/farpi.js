
var ws;

function onLoad() {
    
    ws = new WebSocket("ws://localhost:8888/farpi");

    ws.onmessage = function(e) {
       document.getElementById("message_content").innerHTML = e.data;
       received = JSON.parse(e.data);
    };
}

function sendMsg() {
    ws.send(document.getElementById('msg').value);
}
