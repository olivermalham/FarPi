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
