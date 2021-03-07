
export class Pin {
    state: boolean = false;
}

export class State {
    frame: Number = 0;
    message: string = "";
    bcm00: Pin;

    constructor(packet: any){
        this.frame = packet.cycle;
        this.message = packet.message;
        this.bcm00 = new Pin();
        if (packet["bcm00"]){
            this.bcm00.state = packet["bcm00"].state;
        }
    }
}
