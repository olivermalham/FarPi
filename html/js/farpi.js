
var FarPi = {
    /*
        Primary interface into the FarPi system.
    */

    // Send a message back to the server
    sendMsg: function() {
        this.socket.send(document.getElementById('msg').value);
    },

    // Called when the page is loaded. Opens a websocket connection to the server
    // and registers the callback to handle the returned server state.
    onLoad: function(target) {

        this.socket = new WebSocket(target);

        this.socket.onmessage = function(e) {
            //console.log(e.data);
            FarPi.state = JSON.parse(e.data);
            for(var i in FarPi._callbacks){
                FarPi._callbacks[i]();
            }
        };
    },

    // Private list of call back functions that get called whenever
    // the state gets refreshed by the server
    _callbacks: [],
    registerCallback: function(callback){
        this._callbacks.push(callback);
    },

    // State attribute is populated by JSON decoding server response
    state: {},

    // Web-socket connection to the server
    socket: undefined
}
