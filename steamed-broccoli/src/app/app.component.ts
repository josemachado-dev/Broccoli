import { Component } from '@angular/core';


class Row {
  data : string[]

  constructor(columns : any[]) {
    this.data = columns.map((column) => "-");
  }
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor() {
    document
      .getElementsByTagName("body")[0]
      .addEventListener('click', (event) => {
        this.editColumnTitleIndex = -1;
      }
    )
  }
  
  title = 'steamed-broccoli';

  columns : string[] = [];
  rows : Row[] = [];

  editColumnTitleIndex = -1;

  editColumnTitle(index, event) {
    event.stopImmediatePropagation();
    this.editColumnTitleIndex = index;
  }

  addColumn() {
    this.columns.push("hello");
    let a = this.rows.map((row) => {
      for (let i = row.data.length; i < this.columns.length; ++i) {
        row.data.push("0")
      }
    })
  }

  addRow() {
    this.rows.push(new Row(this.columns));
  }

  removeRow(i : number) {
    this.rows.splice(i,1);
  }
}
