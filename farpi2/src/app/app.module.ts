import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeartbeatComponent } from './controls/heartbeat/heartbeat.component';

import { FarPiHostService } from './far-pi-host.service';

@NgModule({
  declarations: [
    AppComponent,
    HeartbeatComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    FarPiHostService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

