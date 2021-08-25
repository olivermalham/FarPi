import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatProgressBarModule } from '@angular/material/progress-bar';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeartbeatComponent } from './controls/heartbeat/heartbeat.component';

import { FarPiHostService } from './far-pi-host.service';
import { MessageboxComponent } from './controls/messagebox/messagebox.component';
import { LedComponent } from './controls/led/led.component';
import { ToolbarComponent } from './controls/marvin_toolbar/marvin_toolbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    HeartbeatComponent,
    MessageboxComponent,
    LedComponent,
    ToolbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatGridListModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatProgressBarModule
  ],
  providers: [
    FarPiHostService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

