import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Marvin Control Centre';
  vision_server = "192.168.0.142:5000"; // Note: Marvin uses iptables to forward traffic for port 5000 to the Nano
}
