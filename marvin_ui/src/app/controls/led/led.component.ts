import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';

@Component({
  selector: 'app-led',
  templateUrl: './led.component.html',
  styleUrls: ['./led.component.scss']
})
export class LedComponent implements OnInit {

  public state: boolean = false;

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
  }

}
