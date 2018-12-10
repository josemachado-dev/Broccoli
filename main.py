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
import csv
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
    
    def export(self, phrasesdb, filename):
        with open(filename, "w") as file:
            fieldnames = ['text', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for key, item in phrasesdb.items():
                writer.writerow(key)

#Defining the app and its funtions
class Broccoli:
    #This serves merly to test new functions, and see if they're being called when they should
    def debug(self):
        print("debug was called")

    def __init__(self, db):
        self.phrasesdb = db.phrases
        self.db = db
        self.db.currentfilename = "Untitled-1.json"

        #Definition of root window
        self.rootwindow = tk.Tk()
        self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")

        self.tableframe = tk.Frame(self.rootwindow)
        self.tableframe.pack(fill=tk.X)
        self.enteryframe = tk.Frame(self.rootwindow)
        self.enteryframe.pack(fill=tk.X)

        self.assembletopmenu()
        self.assembletable()
        self.assemblestatusbar()

        #Root Window draw
        self.rootwindow.update()
        self.rootwindow.mainloop()

    def assembletable(self):
        self.table = tbl.Table(self.tableframe, ["index", "text", "category"], column_minwidths=[None, None, None])
        self.table.pack(padx=10,pady=10)

        self.createinputs()

        self.rootwindow.update()
        self.rootwindow.geometry("%sx%s"%(self.rootwindow.winfo_reqwidth(),250))

    def createinputs(self):
        self.enterText = tk.Entry(self.enteryframe)
        self.enterText.grid(row=1, column=0)
        self.enterCategory = tk.Entry(self.enteryframe)
        self.enterCategory.grid(row=1, column=1)
        self.enterCategory.bind("<Return>", (lambda event: self.addline()))

    def newfile(self):
        self.updatestatusbar("Cleaning table")
        self.table._pop_n_rows(len(self.phrasesdb))

        self.updatestatusbar("Creating new file")
        self.db.currentfilename = "Untitled-1.json"
        self.db.savedbefore = False
        self.phrasesdb = []

        self.updatestatusbar("")
        self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
        self.rootwindow.update()

    def openfile(self):
        self.updatestatusbar("Opening file...")
        f = tk.filedialog.askopenfilename(filetypes=[("json","*.json")])
        if f is None:
            return
        
        self.updatestatusbar("Opening file at " + f)
        self.db.currentfilename = f
        self.db.savedbefore = True

        self.updatestatusbar("")
        self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
        self.rootwindow.update()

        with open(f if f is not None else self.db.currentfilename, "r") as file:
            data = json.load(file)
            for thing in data:
                newobj = {"text": thing["text"], "category": thing["category"]}
                self.phrasesdb.append(newobj)

                ##This shows new obj on the table
                self.table.insert_row([len(self.phrasesdb), newobj["text"], newobj["category"]])

                self.enterText.delete(0, tk.END)
                self.enterCategory.delete(0, tk.END)

                self.rootwindow.update()

                ##This will allow to edit the line
                ##NEEDS REWORK
                ##newesttext.bind("<Double-Button-1>", self.beginedit)
                ##newestcategory.bind("<Double-Button-1>", self.beginedit)

        ##This pushes the input fields to the bottom of the list
        self.enterText = tk.Entry(self.enteryframe)
        self.enterText.grid(row=1, column=0)
        self.enterCategory = tk.Entry(self.enteryframe)
        self.enterCategory.grid(row=1, column=1)
        self.addlinebutton = tk.Button(self.enteryframe, text=" + ", command=self.addline)
        self.addlinebutton.grid(row=1, column=2)

        self.rootwindow.update()

    def savefile(self):
        if self.db.savedbefore:
            self.updatestatusbar("Saving file to " + self.db.currentfilename)
            self.db.save()

            self.updatestatusbar("")
            self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
            self.rootwindow.update()
        else:
            self.savefileas()

    def savefileas(self):
        self.updatestatusbar("Saving file...")

        f = tk.filedialog.asksaveasfilename(filetypes=[("json", "*.json")], defaultextension=".json", initialfile=self.db.currentfilename)

        self.updatestatusbar("Saving file to " + f)

        if f is None:
           return

        self.db.currentfilename = f
        self.db.savedbefore = True
        self.db.save(f)

        self.updatestatusbar("")
        self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
        self.rootwindow.update()

    def exitapp(self):
        self.rootwindow.destroy()

    def reportbug(self):
        webbrowser.open("https://github.com/josemachado-dev/improved-broccoli/issues/new/choose", new=2, autoraise=True)
    
    def sendfeedback(self):
        webbrowser.open("https://github.com/josemachado-dev/improved-broccoli/issues/new/choose", new=2, autoraise=True)

    def showdocumentation(self):
        #url should be updated if documentation changes places, for example, a wiki is created
        webbrowser.open("https://github.com/josemachado-dev/improved-broccoli", new=2, autoraise=True)

    def addline(self):
        #Add obj to list

        ##This creates new obj with values from the input fields, and inserts it in the list
        newobj = {"text": self.enterText.get(), "category": self.enterCategory.get()}
        self.phrasesdb.append(newobj)

        self.table.insert_row([len(self.phrasesdb), newobj["text"], newobj["category"]])

        self.enterText.delete(0, tk.END)
        self.enterCategory.delete(0, tk.END)

        self.rootwindow.update()

        ##This will allow to edit the line
        ##NEEDS REWORK
        ##newesttext.bind("<Double-Button-1>", self.beginedit)
        ##newestcategory.bind("<Double-Button-1>", self.beginedit)

    def beginedit(self, event):
        #Edit obj in list, given it's index

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

    def editline(self, event, edittext, editcategory):
        #Commits the edit of a given line

        ##Since the first row (row[0]) is the title row, the index of the obj is one less than the row it's shown in
        row = event.widget.grid_info()["row"]
        index = row - 1
        self.phrasesdb[index].update({"text": edittext.get(), "category": editcategory.get()})

        ##This delets the entrys on the row to be edited, to give space for new labels
        for entry in self.tableframe.grid_slaves():
            if int(entry.grid_info()["row"]) == row and int(entry.grid_info()["column"]) > 0:
                entry.grid_forget()

        ##This shows edited obj on the table
        self.table.cell(index,0, index)
        self.table.cell(index,1, edittext.get())
        self.table.cell(index,2, editcategory.get())
        
        #NEEDS REWORK
        #editedtext.bind("<Double-Button-1>", self.beginedit)
        #editedcategory.bind("<Double-Button-1>", self.beginedit)

    def removeline(self, n):
        #Remove obj from list, given it's index

        self.table.delete_row(n)

    def exportfile(self):
        self.updatestatusbar("Exporting file...")
        f = tk.filedialog.asksaveasfilename(filetypes=[("csv", "*.csv")], defaultextension=".csv", initialfile=self.db.currentfilename)

        self.updatestatusbar("Exporting file to " + f)

        if f is None:
           return

        self.db.export(self.phrasesdb, f)

        self.updatestatusbar("")

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
        self.filesubmenu.add_command(label="Export", command=self.exportfile)

        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Exit", command=self.exitapp)
    
    def createeditmenu(self):
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.editmenu)

        self.editmenu.add_command(label="Undo", command=self.debug)
        self.editmenu.add_command(label="Redo", command=self.debug)

        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.debug)
        self.editmenu.add_command(label="Copy", command=self.debug)
        self.editmenu.add_command(label="Paste", command=self.debug)

    def createhelpmenu(self):
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)

        self.helpmenu.add_command(label="Report a Bug", command=self.reportbug)
        self.helpmenu.add_command(label="Request a Feature", command=self.sendfeedback)

        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Check documentation", command=self.showdocumentation)

    def assembletopmenu(self):
        self.menu = tk.Menu(self.rootwindow)
        self.rootwindow.config(menu=self.menu)

        self.createfilemenu()
        self.createeditmenu()
        self.createhelpmenu()

    def assemblestatusbar(self):
        self.status = tk.Label(self.rootwindow, text="", bd = 1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def updatestatusbar(self, text):
        self.status.config(text=text)
        self.rootwindow.update()

db = DB()
broccoli = Broccoli(db)