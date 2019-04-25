import { Component, OnInit } from '@angular/core';
import { saveAs } from 'file-saver';
import { stringify } from '@angular/compiler/src/util';

@Component({
  selector: 'app-passive-dialogues',
  templateUrl: './passive-dialogues.component.html',
  styleUrls: ['./passive-dialogues.component.css']
})
export class PassiveDialoguesComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  selectedFile = null;

  scriptName : string = ""
  textareaText : string = ""
  spellcheckActive : Boolean = JSON.parse(localStorage.getItem("spellchecker"));

  onFileSelected(event){
    this.selectedFile = event.target.files[0];
  }

  openScript(){
    if(this.selectedFile != null){
      let fr = new FileReader();

      fr.onload = (e : any) => {
        let loadedFile = JSON.parse(e.target.result);

        this.textareaText = loadedFile;
        
        //Script name = uploaded file name, minus the ".json"
        this.scriptName = this.selectedFile.name.substring( 0, this.selectedFile.name.length - 5);
      };
  
      fr.readAsText(this.selectedFile);
    }
  }

  saveScript(){
    var fileContent = JSON.stringify(this.textareaText);

    var fileToDownload = new Blob([fileContent], {type: "application/json;charset=utf-8"});
    
    if(this.scriptName != ""){
      saveAs(fileToDownload, this.scriptName+".json");
    }else{
      saveAs(fileToDownload, "Broccoli_NewScript.json");
    }
  }
}
