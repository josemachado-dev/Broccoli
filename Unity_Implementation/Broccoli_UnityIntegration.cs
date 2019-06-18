using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

/*
    Create a folder called 'StreamingAssets', if you don't have one already.
    There, you should put your .json files you got from 'Broccoli'.

    If you create subfolders on the StreamingAssets folder, take that into consideration when you're defining the 'filePath'
*/

[System.Serializable]
public class Data {
    public List<string> columns;
    public List<Row> rows;
}

[System.Serializable]
public class Row {
    public List<string> data;
}

public class Broccoli_UnityIntegration : MonoBehaviour
{
    string filePath;
    string jsonString;

    //You can set this up to be between 1 and the number of rows you have
    [Range(1, 3)]public int row;
    //You can set this up to be between 1 and the number of columns you have
    [Range(1, 5)]public int col; 

    void Start()
    {
        //You should change this to the name of your file, for example "/Your_File_Name.json"
        filePath = Application.streamingAssetsPath + "/Brocolli_TestTable.json";
        jsonString = File.ReadAllText(filePath);

        //This will hold the information you have in the .json file you got from 'Broccoli'
        Data broccoliHolder = JsonUtility.FromJson<Data>(jsonString);

        //This prints in the console all your Column Titles
        for(int i = 0; i < broccoliHolder.columns.Count; i++){
            Debug.Log(broccoliHolder.columns[i]);
        }

        //This prints in the console all your Cells, in order
        for(int j = 0; j < broccoliHolder.rows.Count; j++){
            for(int z = 0; z < broccoliHolder.rows[j].data.Count; z++){
                Debug.Log(broccoliHolder.rows[j].data[z]);
            }
        }

        //This prints in the console a given cell, if you pass it the row and column that it is at
        Debug.Log(broccoliHolder.rows[row-1].data[col-1]);
    }

}