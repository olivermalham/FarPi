import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatChipsModule } from '@angular/material/chips';
import { MatInputModule } from '@angular/material/input';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { FarPiHostService } from './far-pi-host.service';

import { HeartbeatComponent } from './controls/heartbeat/heartbeat.component';
import { ConsoleComponent } from './controls/console/console.component';
import { LedComponent } from './controls/led/led.component';
import { ToolbarComponent } from './controls/marvin_toolbar/marvin_toolbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ControlPanelComponent } from './controls/control-panel/control-panel.component';
import { SwitchMomentaryComponent } from './controls/switch-momentary/switch-momentary.component';
import { SwitchToggleComponent } from './controls/switch-toggle/switch-toggle.component';
import { CameraComponent } from './controls/camera/camera.component';
import { DPadComponent } from './controls/d-pad/d-pad.component';

@NgModule({
  declarations: [
    AppComponent,
    HeartbeatComponent,
    ConsoleComponent,
    LedComponent,
    ToolbarComponent,
    ControlPanelComponent,
    SwitchMomentaryComponent,
    SwitchToggleComponent,
    CameraComponent,
    DPadComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatGridListModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatProgressBarModule,
    MatChipsModule,
    MatInputModule
  ],
  providers: [
    FarPiHostService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

