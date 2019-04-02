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

    //Table starts with 1 column and 1 row
    this.addColumn(null);
  }

  tableName : string = "";
  
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

  addColumn(columnName : string) {
    if(this.rows.length == 0 && this.firstRowOrColumn){
      this.firstRowOrColumn = false;
      this.addRow();
    }

    if(columnName == "" || columnName == null){
      this.columns.push("Column Title");
    }else{
      this.columns.push(columnName)
    }

    let a = this.rows.map((row) => {
      for (let i = row.data.length; i < this.columns.length; ++i) {
        row.data.push("")
      }
    })
  }

  removeColumn(i : number) {
    this.columns.splice(i,1);
    for(var j = 0; j < this.rows.length; j++){
      this.rows[j].data.splice(i,1);
    }

    if(this.columns.length == 0){
      this.rows.splice(0, this.rows.length);
      this.firstRowOrColumn = true;
    }
  }

  addRow() {
    if(this.columns.length == 0 && this.firstRowOrColumn){
      this.firstRowOrColumn = false;
      this.addColumn(null);
    }

    this.rows.push(new Row(this.columns));
  }

  removeRow(i : number) {
    this.rows.splice(i,1);
  }

  saveTable(){
    let columns = this.columns;
    let rows = this.rows;

    var fileContent = JSON.stringify( { columns, rows } );

    var fileToDownload = new Blob([fileContent], {type: "application/json;charset=utf-8"});
    
    if(this.tableName != ""){
      saveAs(fileToDownload, this.tableName+".json");
    }else{
      saveAs(fileToDownload, "SB_NewTable.json");
    }
  }

  onFileSelected(event){
    this.selectedFile = event.target.files[0];
  }

  openTable(){
    if(this.selectedFile != null){
      let fr = new FileReader();

      fr.onload = (e : any) => {
        let loadedFile = JSON.parse(e.target.result);

        this.columns = loadedFile.columns;
        this.rows = loadedFile.rows;
      };
  
      fr.readAsText(this.selectedFile);
    }
  }

  openTemplate(){
    this.columns = [];
    this.rows = [];

    this.addColumn("Character");
    this.addColumn("Line")

    this.addRow();
  }

  trackByIndex(col, row = undefined) {
    return () => { return `c_${col}-r_${row}` }
  }

}
