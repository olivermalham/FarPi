
export class Pin {
    state: boolean = false;
}

export class State {
    frame: Number = 0;
    message: string = "";
    bcm00: Pin;
    bcm01: Pin;
    bcm02: Pin;
    bcm03: Pin;

    constructor(packet: any){
        this.frame = packet.cycle;
        this.message = packet.message;
        
        this.bcm00 = new Pin();
        if (packet["bcm00"]){
            this.bcm00.state = packet["bcm00"].state;
        }

        this.bcm01 = new Pin();
        if (packet["bcm01"]){
            this.bcm01.state = packet["bcm01"].state;
        }

        this.bcm02 = new Pin();
        if (packet["bcm02"]){
            this.bcm02.state = packet["bcm02"].state;
        }

        this.bcm03 = new Pin();
        if (packet["bcm03"]){
            this.bcm03.state = packet["bcm03"].state;
        }
    }
}
