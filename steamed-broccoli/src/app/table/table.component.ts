import { Component, OnInit } from '@angular/core';
import { saveAs } from 'file-saver';
import { stringify } from '@angular/compiler/src/util';

class Row {
  data : string[]

  constructor(columns : any[]) {
    this.data = columns.map((column) => "");
  }
}

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})

export class TableComponent {
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
  firstRowOrColumn = true;

  editColumnTitleIndex = -1;

  selectedFile = null;
  
  spellcheckActive = true;


  editColumnTitle(index, event) {
    event.stopImmediatePropagation();
    this.editColumnTitleIndex = index;
  }

  addColumn() {
    if(this.rows.length == 0 && this.firstRowOrColumn){
      this.firstRowOrColumn = false;
      this.addRow();
    }

    this.columns.push("Column Title");
    let a = this.rows.map((row) => {
      for (let i = row.data.length; i < this.columns.length; ++i) {
        row.data.push("")
      }
    })
  }

  removeColumn() {
    console.error("Needs to be implemented")
  }

  addRow() {
    if(this.columns.length == 0 && this.firstRowOrColumn){
      this.firstRowOrColumn = false;
      this.addColumn();
    }

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
    saveAs(fileToDownload, "SB_save.json");
  }

  onFileSelected(event){
    this.selectedFile = event.target.files[0];
  }

  openTable(){
    if(this.selectedFile != null){
      let fr = new FileReader();

      fr.onload = (e : any) => {
        console.log(JSON.parse(e.target.result))
      };
  
      fr.readAsText(this.selectedFile);
    }
  }

  trackByIndex(col, row = undefined) {
    return () => { return `c_${col}-r_${row}` }
  }

}
