import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { FarPiHostService } from '../../far-pi-host.service';

@Component({
  selector: 'console',
  templateUrl: './console.component.html',
  styleUrls: ['./console.component.scss']
})
export class ConsoleComponent implements OnInit {
  @ViewChild('consoleText') private myScrollContainer: ElementRef;
  public buffer: string = "";

  public command_line: string = "";

  constructor(private farpi_service: FarPiHostService) { }

  ngOnInit(): void {
    this.farpi_service.state.subscribe(value=>this.update(value));
  }

  update(state: any){
    if (state.message) {
      this.buffer = this.buffer + "Marvin > " + state.message + "\n";
      this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
    };
    if (state.error) {
      this.buffer = this.buffer + "ERROR > " + state.error + "\n";
      this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
    };
  }

  send_command(){
    console.log("Send command: " + this.command_line);
    this.buffer = this.buffer + "Send > " + this.command_line + "\n";
    this.farpi_service.send_command("commandLine.action_command", {command: this.command_line});
    this.command_line = "";
  }

}
