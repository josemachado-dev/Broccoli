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
    this.addColumn();
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
        //There is a weird bug happening where
        //there is an extra ',\n'
        //if there is an odd number of lines with a even number of rows
        //and maybe or if you have an even number of lines with an odd number of rows

        //need to fix ASAP
    });

    fileToPackt += "\n]"

    var fileToDownload = new Blob([fileToPackt], {type: "application/json;charset=utf-8"});
    
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

        if(loadedFile.length != 0){

          this.columns = [];

          for(let i = 0; i < loadedFile.length; i++){
            this.columns.push(...Object.keys(loadedFile[i]));
          }

        }else{
          window.alert("File is empty.");
        }
      };
  
      fr.readAsText(this.selectedFile);

      //This makes it so the table name is the same as the uploaded file name, minus the ".json"
      let str = this.selectedFile.name;
      this.tableName = str.substring( 0, str.length - 5);
    }
  }

  trackByIndex(col, row = undefined) {
    return () => { return `c_${col}-r_${row}` }
  }

}
