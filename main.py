#External libraries
from tkinter import *

#Each obj on the list is a full line on the table
#Each line is as follows
#Index | Text  | Category
phrasesdb = []


#Add obj to list
def addline():
    ##This creates new obj with values from the input fields, and inserts it in the list
    phrasesdb.append({"text": newtext.get(), "category": newcategory.get()})
    
    ##This shows new obj on the table
    newesttext = Label(tableframe, text=newtext.get())
    newestcategory = Label(tableframe, text=newcategory.get())

    newesttext.grid(row=len(phrasesdb), column=1, sticky=W)
    newestcategory.grid(row=len(phrasesdb), column=2, sticky=W)

    ##This clears the input flields
    newtext.delete(0, END)
    newcategory.delete(0, END)

    ##This pushes the input fields to the bottom of the list
    nextindex = Label(tableframe, text=(len(phrasesdb)+1))
    nextindex.grid(row=(len(phrasesdb)+1))
    newtext.grid(row=(len(phrasesdb)+1), column=1)
    newcategory.grid(row=(len(phrasesdb)+1), column=2)
    addlinebutton.grid(row=(len(phrasesdb)+1), column=3)

#Add all the objs from another list to this list
##Not sure why I would want this, yet. Maybe to allow merging of lists?
def addmultiple(list):
    phrasesdb.extend(list)

#Edit obj in list, given it's index
def editline(n, text, category):
    phrasesdb[n].update({"text": text, "category": category})

#Remove obj from list, given it's index
def removeline(n):
    phrasesdb.remove(phrasesdb[n])


#Definition of root window
rootwindow = Tk()
rootwindow.title("improved-broccoli")


##Table showing content
tableframe = Frame(rootwindow)
tableframe.pack(fill=X)

##This creates the title of the table
indextitle = Label(tableframe, text="index")
texttitle = Label(tableframe, text="text")
categorytitle = Label(tableframe, text="category")

indextitle.grid(row=0)
texttitle.grid(row=0, column=1)
categorytitle.grid(row=0, column=2)

    ###############################################
    # The new objs from the list go in the middle #
    ###############################################

##This creates the first input fields
nextindex = Label(tableframe, text=(len(phrasesdb)+1))
newtext = Entry(tableframe)
newcategory = Entry(tableframe)
addlinebutton = Button(tableframe, text=" + ", command=addline)

nextindex.grid(row=(len(phrasesdb)+1))
newtext.grid(row=(len(phrasesdb)+1), column=1)
newcategory.grid(row=(len(phrasesdb)+1), column=2)
addlinebutton.grid(row=(len(phrasesdb)+1), column=3)

#Root Window draw
rootwindow.mainloop()
