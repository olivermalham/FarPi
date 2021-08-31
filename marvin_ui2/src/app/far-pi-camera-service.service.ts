import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { webSocket } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root'
})
export class FarPiCameraServiceService {

  //private _state: BehaviorSubject<State> = new BehaviorSubject(new State(""));

  //public readonly state: Observable<State> = this._state.asObservable();

  socket = webSocket('ws://localhost:8889/camera');

  constructor() {
    this.socket.subscribe(
      msg => this.handle_update(msg),
      err => this.handle_error(err),
      () => this.handle_closed
    );
  }

  handle_update(packet){
    // Called whenever there is a message from the server.
    //this._state.next(new State(packet));
    if (packet.data instanceof Blob) {
      let image = URL.createObjectURL(packet.data);
      // image.onload = function() { URL.revokeObjectURL(image.src) }
      }
  }
  

  handle_error(error){
    // Called if at any point WebSocket API signals some kind of error.
    console.log('Error!' + error);
  }

  handle_closed(){
    // Called when connection is closed (for whatever reason).
    console.log('complete')
  }

  send_command(action, parameters){

    let packet = { action: action, parameters: parameters};

    console.log('send command ' + packet)
    this.socket.next(packet);
  }
}


/*

    ws_imagestream = new_web_socket('imagestream');

    ws_imagestream.onmessage = function(e) {
        var interval = parseInt($('#fps').val());
        if (e.data instanceof Blob) {
            if (interval > 0) {
                update_fps()
                image.src = URL.createObjectURL(e.data);
                image.onload = function() {
                    URL.revokeObjectURL(image.src);
                }
            }
        }
        if (window.stream_mode == "get") {
            setTimeout(function(){ws_imagestream.send('?')}, interval);
        }
    }

    ws_imagestream.onopen = function() {
        console.log('connected ws_imagestream...');
        ws_imagestream.send('?');
    };
    ws_imagestream.onclose = function() {
        console.log('closed ws_imagestream');
    };
    ws_imagestream.send('?');
});

function new_web_socket(uri_path) {
    var protocol = 'ws:';
    if (window.location.protocol === 'https:') {
        protocol = 'wss:';
    }
    var host = window.location.host;
    var path = window.location.pathname;
    var url = protocol + '//' + host + path + uri_path;
    var ws = new WebSocket(url);
    console.log(url);
    return ws;
}
*/