import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-user-preferences',
  templateUrl: './user-preferences.component.html',
  styleUrls: ['./user-preferences.component.css']
})

//export class Languages {
//  public id: string;
//  public name: string;
//}


export class UserPreferencesComponent implements OnInit {

  constructor() { }

  languages: any[];

  ngOnInit() {
    this.languages=[
      {id: "en", name: "English"},
      {id: "pt-pt", name: "Portuguese"},
      {id: "fr", name: "French"},
      {id: "es", name: "Spanish"},
    ]
  }

}
