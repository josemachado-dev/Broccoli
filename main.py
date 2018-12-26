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

#Internal libraries
import table as tbl
import spellchecker

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
    def debug(self):
        #This serves merly to test new functions, and see if they're being called when they should
        print("debug was called")

    def __init__(self, db):
        self.phrasesdb = db.phrases
        self.db = db
        self.db.currentfilename = "Untitled-1.json"

        #Definition of root window
        self.rootwindow = tk.Tk()
        self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
        self.rootwindow.state("zoomed")

        self.assembletopmenu()
        self.assembletable()
        self.assemblestatusbar()

        self.keybinds()

        #Root Window draw
        self.rootwindow.update()
        self.rootwindow.mainloop()
    
    def keybinds(self):
        #File Menu Shortcuts
        self.rootwindow.bind("<Control-n>", lambda event: self.newfile())
        self.rootwindow.bind("<Control-s>", lambda event: self.savefile())
        self.rootwindow.bind("<Control-S>", lambda event: self.debug())
        self.rootwindow.bind("<Control-o>", lambda event: self.openfile())
        self.rootwindow.bind("<Control-e>", lambda event: self.exportfile())

        #Edit Menu Shortcuts
        self.rootwindow.bind("<Control-z>", lambda event: self.debug()) #Will serve as "undo"
        self.rootwindow.bind("<Control-y>", lambda event: self.debug()) #Will serve as "redo"

        #Help Menu Shortcuts
        self.rootwindow.bind("<F1>", lambda event: self.showdocumentation())

        #Assorted Shortcuts
        self.enterText.bind("<Return>", lambda event: self.entercategory.focus_set())
        self.entercategory.bind("<Return>", lambda event: self.addline())

        self.indexedit.bind("<Return>", lambda event: self.edittext.focus_set())
        self.edittext.bind("<Return>", lambda event: self.editcategory.focus_set())
        self.editcategory.bind("<Return>", lambda event: self.editline())

    def assembletable(self):
        self.tableframe = tk.Frame(self.rootwindow)
        self.tableframe.pack(fill=tk.X)

        self.table = tbl.Table(self.tableframe, ["index", "text", "category"], column_minwidths=[None, None, None])
        self.columns = 3
        self.table.pack(padx=10,pady=10)

        self.createinputs()

        self.rootwindow.update()
        self.rootwindow.geometry("%sx%s"%(self.rootwindow.winfo_reqwidth(),250))

    def createinputs(self):
        self.enteryframe = tk.Frame(self.rootwindow)
        self.enteryframe.pack(fill=tk.X)

        self.newindex = tk.Label(self.enteryframe, text="#") #index (doesn't auto update yet)
        self.newindex.grid(row=1, column=0)
        self.enterText = tk.Entry(self.enteryframe)
        self.enterText.grid(row=1, column=1)
        self.entercategory = tk.Entry(self.enteryframe)
        self.entercategory.grid(row=1, column=2)

        self.breakindex = tk.Label(self.enteryframe, text="-----------")
        self.breakindex.grid(row=2, column=0)
        self.breakindex = tk.Label(self.enteryframe, text="VV Edit line in table VV")
        self.breakindex.grid(row=3, column=0)

        self.indexedittitle = tk.Label(self.enteryframe, text="index")
        self.indexedittitle.grid(row=4, column=0)
        self.edittexttitle = tk.Label(self.enteryframe, text="text")
        self.edittexttitle.grid(row=4, column=1)
        self.editcategorytitle = tk.Label(self.enteryframe, text="category")
        self.editcategorytitle.grid(row=4, column=2)

        self.indexedit = tk.Entry(self.enteryframe)
        self.indexedit.grid(row=5, column=0)
        self.edittext = tk.Entry(self.enteryframe)
        self.edittext.grid(row=5, column=1)
        self.editcategory = tk.Entry(self.enteryframe)
        self.editcategory.grid(row=5, column=2)

    def newfile(self):
        self.updatestatusprocess("Cleaning table")
        self.table._pop_n_rows(len(self.phrasesdb))

        self.updatestatusprocess("Creating new file")
        self.db.currentfilename = "Untitled-1.json"
        self.db.savedbefore = False
        self.phrasesdb = []

        self.updatestatusmetrics("Rows: %d | Columns: %d" % (len(self.phrasesdb), self.columns))
        self.updatestatusprocess("")
        self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
        self.rootwindow.update()

    def openfile(self):
        self.updatestatusprocess("Opening file...")
        f = tk.filedialog.askopenfilename(filetypes=[("json","*.json")])
        if f == '':
            self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
            return

        self.updatestatusprocess("Cleaning table")
        self.table._pop_n_rows(len(self.phrasesdb))
        self.phrasesdb = []

        self.updatestatusprocess("Opening file at " + f)
        self.db.currentfilename = f
        self.db.savedbefore = True

        self.updatestatusprocess("")
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
                self.entercategory.delete(0, tk.END)

                self.rootwindow.update()

                ##This will allow to edit the line
                ##NEEDS REWORK
                ##newesttext.bind("<Double-Button-1>", self.beginedit)
                ##newestcategory.bind("<Double-Button-1>", self.beginedit)

        self.updatestatusmetrics("Rows: %d | Columns: %d" % (len(self.phrasesdb), self.columns))
        self.rootwindow.update()

    def savefile(self):
        if self.db.savedbefore:
            self.updatestatusprocess("Saving file to " + self.db.currentfilename)
            self.db.save()

            self.updatestatusprocess("")
            self.rootwindow.title(self.db.currentfilename + " - improved-broccoli")
            self.rootwindow.update()
        else:
            self.savefileas()

    def savefileas(self):
        self.updatestatusprocess("Saving file...")

        f = tk.filedialog.asksaveasfilename(filetypes=[("json", "*.json")], defaultextension=".json", initialfile=self.db.currentfilename)

        self.updatestatusprocess("Saving file to " + f)

        if f == '':
           return

        self.db.currentfilename = f
        self.db.savedbefore = True
        self.db.save(f)

        self.updatestatusprocess("")
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
        newobj = {"text": self.enterText.get(), "category": self.entercategory.get()}
        self.phrasesdb.append(newobj)

        self.table.insert_row([len(self.phrasesdb), newobj["text"], newobj["category"]])

        self.enterText.delete(0, tk.END)
        self.entercategory.delete(0, tk.END)

        self.updatestatusmetrics("Rows: %d | Columns: %d" % (len(self.phrasesdb), self.columns))

        self.enterText.focus_set()
        self.rootwindow.update()

        ##This will allow to edit the line
        ##NEEDS REWORK
        ##newesttext.bind("<Double-Button-1>", self.beginedit)
        ##newestcategory.bind("<Double-Button-1>", self.beginedit)

    def editline(self):
        #Commits the edit of a given line

        self.index = int(self.indexedit.get())
        if(self.edittext != ""):
            self.table.cell(self.index, 1, self.edittext.get())

        if(self.editcategory != ""):
            self.table.cell(self.index, 2, self.editcategory.get())

        #NEEDS REWORK
        #editedtext.bind("<Double-Button-1>", self.beginedit)
        #editedcategory.bind("<Double-Button-1>", self.beginedit)

    def removeline(self, n):
        #Remove obj from list, given it's index

        self.table.delete_row(n)
        self.updatestatusmetrics("Rows: %d | Columns: %d" % (len(self.phrasesdb), self.columns))

    def exportfile(self):
        self.updatestatusprocess("Exporting file...")
        f = tk.filedialog.asksaveasfilename(filetypes=[("csv", "*.csv")], defaultextension=".csv", initialfile=self.db.currentfilename)

        self.updatestatusprocess("Exporting file to " + f)

        if f == '':
           return

        self.db.export(self.phrasesdb, f)

        self.updatestatusprocess("")

    def createfilemenu(self):
        self.filesubmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.filesubmenu)

        self.filesubmenu.add_command(label="New File    Ctrl+n", command=self.newfile)

        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Open    Ctrl+o", command=self.openfile)

        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Save    Ctrl+s", command=self.savefile)
        self.filesubmenu.add_command(label="Save As    Ctrl+Shift+s", command=self.savefileas)

        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Export    Ctrl+e", command=self.exportfile)

        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Exit", command=self.exitapp)
    
    def createeditmenu(self):
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.editmenu)

        self.editmenu.add_command(label="Undo    Ctrl+z", command=self.debug)
        self.editmenu.add_command(label="Redo    Ctrl+y", command=self.debug)

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
        self.helpmenu.add_command(label="Check documentation    F1", command=self.showdocumentation)

    def assembletopmenu(self):
        self.menu = tk.Menu(self.rootwindow)
        self.rootwindow.config(menu=self.menu)

        self.createfilemenu()
        self.createeditmenu()
        self.createhelpmenu()

    def assemblestatusbar(self):
        self.statusframe = tk.Frame(self.rootwindow, bd = 1, relief=tk.SUNKEN)
        self.statusframe.pack(side=tk.BOTTOM, fill=tk.X)

        self.statusprocess = tk.Label(self.statusframe, text="", anchor=tk.W)
        self.statusprocess.pack(side=tk.RIGHT)

        self.statusmetrics = tk.Label(self.statusframe, text="Rows: 0 | Columns: 3", anchor=tk.W)
        self.statusmetrics.pack(side=tk.LEFT)
    
    def updatestatusprocess(self, text):
        self.statusprocess.config(text=text)
        self.rootwindow.update()

    def updatestatusmetrics(self, text):
        self.statusmetrics.config(text=text)
        self.rootwindow.update()

db = DB()
broccoli = Broccoli(db)