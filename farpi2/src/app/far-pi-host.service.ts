import { Injectable } from '@angular/core';
import { webSocket } from 'rxjs/webSocket';
import { Heartbeat } from './models/heartbeat';

@Injectable({
  providedIn: 'root'
})
export class FarPiHostService {

  socket = webSocket('ws://localhost:8888/farpi');

  public heartbeat = new Heartbeat;

  constructor() {
    this.socket.subscribe(
      msg => this.handle_update(msg),
      err => this.handle_error(err),
      () => this.handle_closed
    );
  }

  handle_update(packet){
    // Called whenever there is a message from the server.
    console.log('message received: ' + packet);
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
