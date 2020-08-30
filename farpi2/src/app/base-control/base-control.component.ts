import { Component, OnInit } from '@angular/core';
import { webSocket } from 'rxjs/webSocket';


@Component({
  selector: 'app-base-control',
  templateUrl: './base-control.component.html',
  styleUrls: ['./base-control.component.scss']
})
export class BaseControlComponent implements OnInit {

  socket = webSocket('ws://localhost:8888/farpi');

  constructor() { }

  ngOnInit(): void {
    this.socket.subscribe(
      msg => console.log('message received: ' + msg), // Called whenever there is a message from the server.
      err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
      () => console.log('complete') // Called when connection is closed (for whatever reason).
    );
  }
}
