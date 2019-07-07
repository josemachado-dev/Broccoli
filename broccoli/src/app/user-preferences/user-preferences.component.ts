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

  languages : Languages[];
  spellcheck : Boolean;
  darkMode : Boolean;

  ngOnInit() {
    this.languages=[
      {id: "en", name: "English"},
      {id: "pt-pt", name: "Portuguese"},
      {id: "fr", name: "French"},
      {id: "es", name: "Spanish"},
    ]

    if(!localStorage.getItem("spellchecker")) {
      this.spellcheckStorage();
    }
  }

  spellcheckStorage(){
    this.spellcheck = !this.spellcheck;
    localStorage.setItem("spellchecker", JSON.stringify(this.spellcheck));
  }

  darkModeStorage(){
    this.darkMode = !this.darkMode;
    localStorage.setItem("darkMode", JSON.stringify(this.darkMode));
  }

}
