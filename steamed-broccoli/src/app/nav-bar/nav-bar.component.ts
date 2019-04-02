import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent {

  constructor() { }

  reportBug(){
    window.open("https://github.com/josemachado-dev/improved-broccoli/issues/new/choose", "_blank");
  }

  requestFeature(){
    window.open("https://github.com/josemachado-dev/improved-broccoli/issues/new/choose", "_blank");
  }

}
