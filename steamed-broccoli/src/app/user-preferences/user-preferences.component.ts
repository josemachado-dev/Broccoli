import { Component, OnInit } from '@angular/core';
import { Languages } from './languages';

@Component({
  selector: 'app-user-preferences',
  templateUrl: './user-preferences.component.html',
  styleUrls: ['./user-preferences.component.css']
})

export class UserPreferencesComponent implements OnInit {

  constructor() { }

  languages: Languages[];

  ngOnInit() {
    this.languages=[
      {id: "en", name: "English"},
      {id: "pt-pt", name: "Portuguese"},
    ]
  }

}
