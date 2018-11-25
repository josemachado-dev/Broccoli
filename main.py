#External libraries
import tkinter as tk
import tkinter.filedialog
import json
import webbrowser

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
    def debugevent(self, event):
        print("debug event was called")

    def debug(self):
        print("debug was called")

    #Each obj on the list is a full line on the table
    #Each line is as follows
    #Index | Text  | Category
    def __init__(self, db):
        self.phrasesdb = db.phrases
        self.db = db

        #Definition of root window
        self.rootwindow = tk.Tk()
        self.rootwindow.title("improved-broccoli")

        self.assembletopmenu()

        #Table showing content
        self.tableframe = tk.Frame(self.rootwindow)
        self.tableframe.pack(fill=tk.X)

        ##This creates the title of the table
        self.indextitle = tk.Label(self.tableframe, text="index")
        self.texttitle = tk.Label(self.tableframe, text="text")
        self.categorytitle = tk.Label(self.tableframe, text="category")

        self.indextitle.grid(row=0)
        self.texttitle.grid(row=0, column=1)
        self.categorytitle.grid(row=0, column=2)

        ###############################################
        # The new objs from the list go in the middle #
        ###############################################

        ##This creates the first input fields
        self.nextindex = tk.Label(self.tableframe, text=(len(self.phrasesdb)))
        self.newtext = tk.Entry(self.tableframe)
        self.newcategory = tk.Entry(self.tableframe)
        self.addlinebutton = tk.Button(self.tableframe, text=" + ", command=self.addline)

        self.nextindex.grid(row=(len(self.phrasesdb)+1))
        self.newtext.grid(row=(len(self.phrasesdb)+1), column=1)
        self.newcategory.grid(row=(len(self.phrasesdb)+1), column=2)
        self.addlinebutton.grid(row=(len(self.phrasesdb)+1), column=3)

        self.assemblestatusbar()

        #Root Window draw
        self.rootwindow.mainloop()

    def savefile(self):
        #self.db.save()

        if self.db.savedbefore:
            self.db.save()
        else:
            self.savefileas()


    def savefileas(self):
       filename = "hello.json" #Do interface
       f = tk.filedialog.asksaveasfilename(filetypes=("json", "*.json"))
       if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
           return
       f.close()

       self.db.currentfilename = filename
       self.db.savedbefore = True
       self.db.save(filename)


    def exitapp(self):
        self.rootwindow.destroy()

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

        ##This will allow to edit the line, eventually
        ### preferebly this would go on a different function
        newesttext.bind("<Double-Button-1>", self.beginedit)
        newestcategory.bind("<Double-Button-1>", self.beginedit)

        newesttext.grid(row=len(self.phrasesdb), column=1, sticky=tk.W)
        newestcategory.grid(row=len(self.phrasesdb), column=2, sticky=tk.W)

        ##This clears the input flields
        self.newtext.delete(0, tk.END)
        self.newcategory.delete(0, tk.END)

        ##This pushes the input fields to the bottom of the list
        nextindex = tk.Label(self.tableframe, text=(len(self.phrasesdb)))
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

    #Commits the edit
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
        self.filesubmenu.add_command(label="New File", command=self.debug) #Remove debug, put actual function
        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Open", command=self.debug) #Remove debug, put actual function
        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Save", command=self.savefile)
        self.filesubmenu.add_command(label="Save As", command=self.savefileas)
        self.filesubmenu.add_separator()
        self.filesubmenu.add_command(label="Exit", command=self.exitapp)

    def createhelpmenu(self):
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="Report a Bug", command=self.debug) #Remove debug, put actual function
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