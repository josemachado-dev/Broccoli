import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { CommonModule } from '@angular/common';
import { AppComponent } from './app.component';
import { UserPreferencesComponent } from './user-preferences/user-preferences.component';
import { TableComponent } from './table/table.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { PassiveDialoguesComponent } from './passive-dialogues/passive-dialogues.component';

@NgModule({
  declarations: [
    AppComponent,
    UserPreferencesComponent,
    TableComponent,
    NavBarComponent,
    PassiveDialoguesComponent
  ],
  imports: [
    BrowserModule, FormsModule, CommonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }