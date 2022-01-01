import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.scss']
})
export class CameraComponent implements OnInit {

  @Input()
  public label: string;

  @Input()
  public url: string;

  constructor() { }

  ngOnInit(): void {
  }
}
