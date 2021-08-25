import { Component, OnInit, Input } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';
import { ThrowStmt } from '@angular/compiler';

@Component({
  selector: 'app-heartbeat',
  templateUrl: './heartbeat.component.html',
  styleUrls: ['./heartbeat.component.scss']
})
export class HeartbeatComponent implements OnInit {

  public beat: number = 0;

  public classes= {
    "farpi-HeartBeat": true,
    "farpi-HeartBeatGlow": false
  } ;

  constructor(private farpi_service: FarPiHostService) { }

  ngOnInit(): void {
    this.farpi_service.state.subscribe(value=>this.update(value));
  }

  update(state: any){
    this.beat = state.frame % 2;
    this.classes = {
      "farpi-HeartBeat": true,
      "farpi-HeartBeatGlow": (this.beat > 0)
    }
  }
}
