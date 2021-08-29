import { Component, OnInit } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';

@Component({
  selector: 'console',
  templateUrl: './console.component.html',
  styleUrls: ['./console.component.scss']
})
export class ConsoleComponent implements OnInit {

  public buffer: string = "";

  constructor(private farpi_service: FarPiHostService) { }

  ngOnInit(): void {
    this.farpi_service.state.subscribe(value=>this.update(value));
  }

  update(state: any){
    if (state.message) {
      this.buffer = state.frame + ": " + state.message + "\n" + this.buffer;
    };
  }

}
