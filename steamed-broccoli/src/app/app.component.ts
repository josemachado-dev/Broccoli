import { Component } from '@angular/core';
import { saveAs } from 'file-saver';


class Row {
  data : string[]

  constructor(columns : any[]) {
    this.data = columns.map((column) => "");
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

  saveTable(){
    let fileToPackt = "[\n"

    this.rows.forEach((row, rowIndex, rows) => {
        fileToPackt += "\t{ "
        this.columns.map((column, columnIndex, columns) => {
            fileToPackt += `"${column}": "${row.data[columnIndex]}"${columnIndex + 1 == columns.length ? '': ','}`
        })
        fileToPackt += ` }${rowIndex + 1 == this.columns.length ? '' : ',\n'}`
    });

    fileToPackt += "\n]"

    var fileToDownload = new Blob([fileToPackt], {type: "application/json;charset=utf-8"});
    saveAs(fileToDownload, "stemed-broccoli_save.json");
  }

  trackByIndex(col, row = undefined) {
    return () => { return `c_${col}-r_${row}` }
  }

}
