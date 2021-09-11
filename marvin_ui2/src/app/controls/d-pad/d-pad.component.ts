import { Component, OnInit } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';

@Component({
  selector: 'd-pad',
  templateUrl: './d-pad.component.html',
  styleUrls: ['./d-pad.component.scss']
})
export class DPadComponent implements OnInit {

  constructor(private farpi_service: FarPiHostService) { }

  ngOnInit(): void {
    this.farpi_service.state.subscribe(value=>this.update(value));
  }

  update(state: any){
  }

  action_move_left(){
    console.log("D-Pad Action turn left triggered");
    this.farpi_service.send_command("motion.action_turn", {"angle":-20, "speed":20});
  }

  action_move_right(){
    console.log("D-Pad Action turn right triggered");
    this.farpi_service.send_command("motion.action_turn", {"angle":20, "speed":20});
  }

  action_move_cancel(){
    console.log("D-Pad Action move cancel triggered");
    this.farpi_service.send_command("motion.action_stop", {});
  }

  action_move_forward(){
    console.log("D-Pad Action move forward triggered");
    this.farpi_service.send_command("motion.action_move", {"distance":200, speed:100});
  }

  action_move_back(){
    console.log("D-Pad Action move back triggered");
    this.farpi_service.send_command("motion.action_move", {"distance":-200, speed:100});
  }

  action_head_up(){
    console.log("D-Pad Action head up triggered");
    this.farpi_service.send_command("motion.action_move_head", {"direction":"pitch", "angle":20});
  }

  action_head_down(){
    console.log("D-Pad Action head down triggered");
    this.farpi_service.send_command("motion.action_move_head", {"direction":"pitch", "angle":-20});
  }

  action_head_center(){
    console.log("D-Pad Action head center triggered");
    this.farpi_service.send_command("motion.action_center_head", {});
  }

  action_head_left(){
    console.log("D-Pad Action head left triggered");
    this.farpi_service.send_command("motion.action_move_head", {"direction":"yaw", "angle":-20});
  }

  action_head_right(){
    console.log("D-Pad Action head right triggered");
    this.farpi_service.send_command("motion.action_move_head", {"direction":"yaw", "angle":20});
  }
}
