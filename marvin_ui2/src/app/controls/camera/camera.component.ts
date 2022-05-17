import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.scss']
})
export class CameraComponent implements OnInit {

  // Note: Marvin uses iptables to forward traffic for port 5000 to the Nano
  vision_server = "http://192.168.0.142:5000";

  @Input()
  public label: string;

  @Input()
  public feed: string;

  constructor() { }

  ngOnInit(): void {
  }
}
