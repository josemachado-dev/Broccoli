import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { CommonModule } from '@angular/common';
import { AppComponent } from './app.component';
import { UserPreferencesComponent } from './user-preferences/user-preferences.component';

@NgModule({
  declarations: [
    AppComponent,
    UserPreferencesComponent
  ],
  imports: [
    BrowserModule, FormsModule, CommonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
