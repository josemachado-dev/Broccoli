# How to use Broccoli with Unity?

Start by creating a folder called `StreamingAssets`, if you don't have one already.  
There, you should put the `.json` file you got from **Broccoli**.  
  
In your `Scripts` folder, paste the `Broccoli_UnityIntegration.cs` file.  

<hr>

## And, after you've built the project?
  
After you've built the project, you can make changes to your `.json`, that will reflect on the build executable.  
You'll need to go to your `StreamingAssets` folder on the build
```
Your_Build_Folder
    > Your_Project_Name_Data
        > StreamingAssets
            > [Here you'll find your .json files]
```
If you edit a `.json` file here (or, replace it by a new `.json` file from **Broccoli** that has the same name), the changes will be reflected on the build executable.  