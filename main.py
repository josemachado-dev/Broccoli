#External libraries
import tkinter as tk
import json
import webbrowser

#Each obj on the list is a full line on the table
#Each line is as follows
#Index | Text  | Category
phrasesdb = []

#This serves merly to test new functions, and see if they're being called when they should
def debugevent(event):
    print("debug event was called")
def debug():
    print("debug was called")

def savefile():
    with open("savefile.json", "w") as file:
        json.dump(phrasesdb, file, indent=2)

def exitapp():
    rootwindow.destroy()

def showdocumentation():
    #url should be updated if documentation changes places, for example, a wiki is created
    webbrowser.open("https://github.com/josemachado-dev/improved-broccoli", new=2, autoraise=True)

#Add obj to list
def addline():
    ##This creates new obj with values from the input fields, and inserts it in the list
    newobj = {"text": newtext.get(), "category": newcategory.get()}
    phrasesdb.append(newobj)
    
    ##This shows new obj on the table
    newesttext = tk.Label(tableframe, text=newobj["text"])
    newestcategory = tk.Label(tableframe, text=newobj["category"])

    ##This will allow to edit the line, eventually
    ### preferebly this would go on a different function
    newesttext.bind("<Double-Button-1>", beginedit)
    newestcategory.bind("<Double-Button-1>", beginedit)

    newesttext.grid(row=len(phrasesdb), column=1, sticky=tk.W)
    newestcategory.grid(row=len(phrasesdb), column=2, sticky=tk.W)

    ##This clears the input flields
    newtext.delete(0, tk.END)
    newcategory.delete(0, tk.END)

    ##This pushes the input fields to the bottom of the list
    nextindex = tk.Label(tableframe, text=(len(phrasesdb)))
    nextindex.grid(row=(len(phrasesdb)+1))
    newtext.grid(row=(len(phrasesdb)+1), column=1)
    newcategory.grid(row=(len(phrasesdb)+1), column=2)
    addlinebutton.grid(row=(len(phrasesdb)+1), column=3)

#Add all the objs from another list to this list
##Not sure why I would want this, yet. Maybe to allow merging of lists?
def addmultiple(list):
    phrasesdb.extend(list)

#Edit obj in list, given it's index
def beginedit(event):
    ##Since the first row (row[0]) is the title row, the index of the obj is one less than the row it's shown in
    row = event.widget.grid_info()["row"]

    ##This delets the labels on the row to be edited, to give space for input fields, but keeps the index shown
    for label in tableframe.grid_slaves():
        if int(label.grid_info()["row"]) == row and int(label.grid_info()["column"]) > 0:
            label.grid_forget()

    ##This creates the entrys for the new inputs
    edittext = tk.Entry(tableframe)
    editcategory = tk.Entry(tableframe)
    #editlinebutton = tk.Button(tableframe, text="edit", command=editline)
    editlinebutton = tk.Button(tableframe, text="edit")

    edittext.grid(row=row, column=1)
    editcategory.grid(row=row, column=2)
    editlinebutton.grid(row=row, column=3)

'''
def editline(event):
    ##Since the first row (row[0]) is the title row, the index of the obj is one less than the row it's shown in
    row = event.widget.grid_info()["row"]
    index = row - 1
    phrasesdb[index].update({"text": edittext.get(), "category": editcategory.get()})
    editobj = phrasesdb[index]

    ##This delets the entrys on the row to be edited, to give space for new labels
    for entry in tableframe.grid_slaves():
        if int(entry.grid_info()["row"]) == row and int(entry.grid_info()["column"]) > 0:
            entry.grid_forget()

    ##This shows edited obj on the table
    editedtext = tk.Label(tableframe, text=editobj["text"])
    editedcategory = tk.Label(tableframe, text=editobj["category"])

    editedtext.bind("<Double-Button-1>", beginedit)
    editedcategory.bind("<Double-Button-1>", beginedit)

    editedtext.grid(row=len(phrasesdb), column=1, sticky=tk.W)
    editedcategory.grid(row=len(phrasesdb), column=2, sticky=tk.W)
'''

#Remove obj from list, given it's index
def removeline(n):
    phrasesdb.remove(phrasesdb[n])


#Definition of root window
rootwindow = tk.Tk()
rootwindow.title("improved-broccoli")

#Top Menu
menu = tk.Menu(rootwindow)
rootwindow.config(menu=menu)

filesubmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filesubmenu)
filesubmenu.add_command(label="New File", command=debug) #Remove debug, put actual function
filesubmenu.add_separator()
filesubmenu.add_command(label="Open", command=debug) #Remove debug, put actual function
filesubmenu.add_separator()
filesubmenu.add_command(label="Save", command=savefile)
filesubmenu.add_command(label="Save As", command=debug) #Remove debug, put actual function
filesubmenu.add_separator()
filesubmenu.add_command(label="Exit", command=exitapp)

helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Report a Bug", command=debug)
helpmenu.add_command(label="Check documentation", command=showdocumentation)

#Table showing content
tableframe = tk.Frame(rootwindow)
tableframe.pack(fill=tk.X)

##This creates the title of the table
indextitle = tk.Label(tableframe, text="index")
texttitle = tk.Label(tableframe, text="text")
categorytitle = tk.Label(tableframe, text="category")

indextitle.grid(row=0)
texttitle.grid(row=0, column=1)
categorytitle.grid(row=0, column=2)

    ###############################################
    # The new objs from the list go in the middle #
    ###############################################

##This creates the first input fields
nextindex = tk.Label(tableframe, text=(len(phrasesdb)))
newtext = tk.Entry(tableframe)
newcategory = tk.Entry(tableframe)
addlinebutton = tk.Button(tableframe, text=" + ", command=addline)

nextindex.grid(row=(len(phrasesdb)+1))
newtext.grid(row=(len(phrasesdb)+1), column=1)
newcategory.grid(row=(len(phrasesdb)+1), column=2)
addlinebutton.grid(row=(len(phrasesdb)+1), column=3)

#Lower Status Bar
##############################
# I have to do it eventually #
##############################

#Root Window draw
rootwindow.mainloop()