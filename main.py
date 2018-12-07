#############################################################################
#[not yet named project] aims to be a tool that serves as a bridge          #
#       between game writers and programmers                                #
#   Copyright (C) 2018  José Machado                                        #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    (at your option) any later version.                                    #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>. #
#############################################################################

#External libraries
import tkinter as tk
import tkinter.filedialog
import json
import webbrowser
import table as tbl

#Defining the database and its funtions
class DB:
    def __init__(self):
        self.currentfilename = "autosave.json"
        self.savedbefore = False
        self.phrases = []

    def save(self, filename=None):
        with open(filename if filename is not None else self.currentfilename, "w") as file:
            json.dump(self.phrases, file, indent=2)
            

#Defining the app and its funtions
class Broccoli:
    #This serves merly to test new functions, and see if they're being called when they should
    def debug(self):
        print("debug was called")

    def __init__(self, db):
        self.phrasesdb = db.phrases
        self.db = db

        #Definition of root window
        self.rootwindow = tk.Tk()
        self.rootwindow.title("improved-broccoli")

        self.assembletopmenu()

        self.oldtable()
        self.newtable()

        self.assemblestatusbar()

        #Root Window draw
        self.rootwindow.mainloop()

    def newtable(self):
        table = tbl.Table(self.rootwindow, ["column A", "column B", "column C"], column_minwidths=[None, None, None])
        table.pack(padx=10,pady=10)

        table.set_data([[1,2,3],[4,5,6], [7,8,9], [10,11,12], [13,14,15],[15,16,18], [19,20,21]])
        table.cell(0,0, " a fdas fasd fasdf asdf asdfasdf asdf asdfa sdfas asd sadf ")
    
        table.insert_row([22,23,24])
        table.insert_row([25,26,27])
    
        self.rootwindow.update()
        self.rootwindow.geometry("%sx%s"%(self.rootwindow.winfo_reqwidth(),250))

    def oldtable(self):
        #Table showing content
        self.scrollbar = tk.Scrollbar(self.rootwindow)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tableframe = tk.Frame(self.rootwindow)
        self.tableframe.pack(fill=tk.X)

        ##This creates the title of the table
        self.indextitle = tk.Label(self.tableframe, text="index")
        self.texttitle = tk.Label(self.tableframe, text="text")
        self.categorytitle = tk.Label(self.tableframe, text="category")

        self.indextitle.grid(row=0)
        self.texttitle.grid(row=0, column=1)
        self.categorytitle.grid(row=0, column=2)

        ##This creates the first input fields
        self.nextindex = tk.Label(self.tableframe, text=(len(self.phrasesdb)))
        self.newtext = tk.Entry(self.tableframe)
        self.newcategory = tk.Entry(self.tableframe)
        self.addlinebutton = tk.Button(self.tableframe, text=" + ", command=self.addline)

        self.nextindex.grid(row=(len(self.phrasesdb)+1))
        self.newtext.grid(row=(len(self.phrasesdb)+1), column=1)
        self.newcategory.grid(row=(len(self.phrasesdb)+1), column=2)
        self.addlinebutton.grid(row=(len(self.phrasesdb)+1), column=3)

    def newfile(self):
        self.debug()

    def openfile(self):
        f = tk.filedialog.askopenfilename(filetypes=[("json","*.json")])
        if f is None:
            return
        
        self.db.currentfilename = f
        self.db.savedbefore = True
        #self.db.openf(f)
        with open(f if f is not None else self.db.currentfilename, "r") as file:
            data = json.load(file)
            for thing in data:
                newobj = {"text": thing["text"], "category": thing["category"]}
                self.phrasesdb.append(newobj)

                ##This shows new obj on the table
                index = tk.Label(self.tableframe, text=len(self.phrasesdb))
                newesttext = tk.Label(self.tableframe, text=newobj["text"])
                newestcategory = tk.Label(self.tableframe, text=newobj["category"])
                index.grid(row=len(self.phrasesdb))
                newesttext.grid(row=len(self.phrasesdb), column=1, sticky=tk.W)
                newestcategory.grid(row=len(self.phrasesdb), column=2, sticky=tk.W)

                ##This will allow to edit the line
                newesttext.bind("<Double-Button-1>", self.beginedit)
                newestcategory.bind("<Double-Button-1>", self.beginedit)

        ##This pushes the input fields to the bottom of the list
        nextindex = tk.Label(self.tableframe, text=len(self.phrasesdb) + 1)
        nextindex.grid(row=(len(self.phrasesdb)+1))
        self.newtext.grid(row=(len(self.phrasesdb)+1), column=1)
        self.newcategory.grid(row=(len(self.phrasesdb)+1), column=2)
        self.addlinebutton.grid(row=(len(self.phrasesdb)+1), column=3)

    def savefile(self):
        if self.db.savedbefore:
            self.db.save()
        else:
            self.savefileas()

    def savefileas(self):
       f = tk.filedialog.asksaveasfilename(filetypes=[("json", "*.json")])
       if f is None:
           return

       self.db.currentfilename = f
       self.db.savedbefore = True
       self.db.save(f)

    def exitapp(self):
        self.rootwindow.destroy()

    def reportbug(self):
        self.debug

    def showdocumentation(self):
        #url should be updated if documentation changes places, for example, a wiki is created
        webbrowser.open("https://github.com/josemachado-dev/improved-broccoli", new=2, autoraise=True)

    #Add obj to list
    def addline(self):
        ##This creates new obj with values from the input fields, and inserts it in the list
        newobj = {"text": self.newtext.get(), "category": self.newcategory.get()}
        self.phrasesdb.append(newobj)

        ##This shows new obj on the table
        newesttext = tk.Label(self.tableframe, text=newobj["text"])
        newestcategory = tk.Label(self.tableframe, text=newobj["category"])

        newesttext.grid(row=len(self.phrasesdb), column=1, sticky=tk.W)
        newestcategory.grid(row=len(self.phrasesdb), column=2, sticky=tk.W)

        ##This will allow to edit the line
        newesttext.bind("<Double-Button-1>", self.beginedit)
        newestcategory.bind("<Double-Button-1>", self.beginedit)

        ##This clears the input flields
        self.newtext.delete(0, tk.END)
        self.newcategory.delete(0, tk.END)

        ##This pushes the input fields to the bottom of the list
        nextindex = tk.Label(self.tableframe, text=len(self.phrasesdb))
        nextindex.grid(row=(len(self.phrasesdb)+1))
        self.newtext.grid(row=(len(self.phrasesdb)+1), column=1)
        self.newcategory.grid(row=(len(self.phrasesdb)+1), column=2)
        self.addlinebutton.grid(row=(len(self.phrasesdb)+1), column=3)

    #Edit obj in list, given it's index
    def beginedit(self, event):
        ##Since the first row (row[0]) is the title row, the index of the obj is one less than the row it's shown in
        row = event.widget.grid_info()["row"]

        ##This delets the labels on the row to be edited, to give space for input fields, but keeps the index shown
        for label in self.tableframe.grid_slaves():
            if int(label.grid_info()["row"]) == row and int(label.grid_info()["column"]) > 0:
                label.grid_forget()

        ##This creates the entrys for the new inputs
        edittext = tk.Entry(self.tableframe)
        editcategory = tk.Entry(self.tableframe)
        editlinebutton = tk.Button(self.tableframe, text="edit")
        editlinebutton.bind("<Button-1>", lambda event: self.editline(event, edittext, editcategory))

        edittext.grid(row=row, column=1)
        editcategory.grid(row=row, column=2)
        editlinebutton.grid(row=row, column=3)

    #Commits the edit of a given line
    def editline(self, event, edittext, editcategory):
        ##Since the first row (row[0]) is the title row, the index of the obj is one less than the row it's shown in
        row = event.widget.grid_info()["row"]
        index = row - 1
        self.phrasesdb[index].update({"text": edittext.get(), "category": editcategory.get()})
        editobj = self.phrasesdb[index]

        ##This delets the entrys on the row to be edited, to give space for new labels
        for entry in self.tableframe.grid_slaves():
            if int(entry.grid_info()["row"]) == row and int(entry.grid_info()["column"]) > 0:
                entry.grid_forget()

        ##This shows edited obj on the table
        editedtext = tk.Label(self.tableframe, text=editobj["text"])
        editedcategory = tk.Label(self.tableframe, text=editobj["category"])

        editedtext.bind("<Double-Button-1>", self.beginedit)
        editedcategory.bind("<Double-Button-1>", self.beginedit)

        editedtext.grid(row=row, column=1, sticky=tk.W)
        editedcategory.grid(row=row, column=2, sticky=tk.W)

    #Remove obj from list, given it's index
    def removeline(self, n):
        self.phrasesdb.remove(self.phrasesdb[n])

    def createfilemenu(self):
        self.filesubmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.filesubmenu)
        self.filesubmenu.add_command(label="New File", command=self.newfile)
        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Open", command=self.openfile)
        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Save", command=self.savefile)
        self.filesubmenu.add_command(label="Save As", command=self.savefileas)
        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Exit", command=self.exitapp)

    def createhelpmenu(self):
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="Report a Bug", command=self.reportbug)
        self.helpmenu.add_command(label="Check documentation", command=self.showdocumentation)

    def assembletopmenu(self):
        self.menu = tk.Menu(self.rootwindow)
        self.rootwindow.config(menu=self.menu)

        self.createfilemenu()
        self.createhelpmenu()

    def assemblestatusbar(self):
        self.status = tk.Label(self.rootwindow, text="DEBUG::STATUS BAR IS WORKING", bd = 1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)


db = DB()
broccoli = Broccoli(db)
