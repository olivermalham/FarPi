import { Component, OnInit } from '@angular/core';
import { webSocket } from 'rxjs/webSocket';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.scss']
})
export class CameraComponent implements OnInit {

  socket = webSocket({url: 'ws://localhost:8889/imagestream',
                      deserializer: msg => msg});
  image;

  constructor(private sanitizer: DomSanitizer) {
    this.socket.subscribe(
      msg => this.handle_update(msg),
      err => this.handle_error(err),
      () => this.handle_closed
    );
    //this.socket.next("?");
    //this.image = document.getElementById("camera-feed");
  }

  ngOnInit(): void {
  }

  handle_update(packet){
    // Called whenever there is a message from the server.
    if (packet.data instanceof Blob) {
      if (this.image) {
        URL.revokeObjectURL(this.image.changingThisBreaksApplicationSecurity);
      }
      this.image = this.sanitizer.bypassSecurityTrustResourceUrl(URL.createObjectURL(packet.data));
      // image.onload = function() { URL.revokeObjectURL(image.src) }
    }
  }

  onload(){
    URL.revokeObjectURL(this.image);
  }
  
  handle_error(error){
    // Called if at any point WebSocket API signals some kind of error.
    console.log('Error!' + error);
  }

  handle_closed(){
    // Called when connection is closed (for whatever reason).
    console.log('complete')
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
}*/