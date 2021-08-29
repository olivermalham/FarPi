import { Component, OnInit, Input } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';

@Component({
  selector: 'led',
  templateUrl: './led.component.html',
  styleUrls: ['./led.component.scss']
})
export class LedComponent implements OnInit {

  public state: boolean = false;
  public stateColour: string = "none";

  @Input() 
  public label: string;

  @Input() 
  public pin: string;

  constructor(private farpi_service: FarPiHostService) { }

  ngOnInit(): void {
    this.farpi_service.state.subscribe(value=>this.update(value));
  }

  update(state: any){
    this.state = state[this.pin].state;
    if(this.state) {
      this.stateColour = "primary";
    } else {
      this.stateColour = "none";
    }
  }

}
