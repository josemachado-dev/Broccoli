import { Component, OnInit } from '@angular/core';

class Languages {
  public id: string;
  public name: string;
}

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
      {id: "fr", name: "French"},
      {id: "es", name: "Spanish"},
    ]
  }

}
