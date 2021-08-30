import { Component, OnInit, Input } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';

@Component({
  selector: 'switch-momentary',
  templateUrl: './switch-momentary.component.html',
  styleUrls: ['./switch-momentary.component.scss']
})
export class SwitchMomentaryComponent implements OnInit {

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

  action_down(){
    console.log("Action down triggered");
    this.farpi_service.send_command(this.pin + ".action_set", {value: true});
  }

  action_up(){
    console.log("Action up triggered");
    this.farpi_service.send_command(this.pin + ".action_set", {value: false});
  }

}
