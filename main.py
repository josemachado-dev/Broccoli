#External libraries
from tkinter import *

#Each obj on the list is a full line on the table
#Each line is as follows
#Index | Text  | Category
phrasesdb = []


#Add obj to list
def addline(text, category):
    phrasesdb.append({"text": text, "category": category})

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


##Table showing content
tableframe = Frame(rootwindow)
tableframe.pack()

indextitle = Label(tableframe, text="index")
texttitle = Label(tableframe, text="text")
categorytitle = Label(tableframe, text="category")

indextitle.grid(row=0)
texttitle.grid(row=0, column=1)
categorytitle.grid(row=0, column=2)

            #############################################
            # In the middle goes the objs from the list #
            #############################################

nextindex = Label(tableframe, text=(len(phrasesdb)+1))
newtext = Entry(tableframe)
newcategory = Entry(tableframe)
addlinebutton = Button(tableframe, text=" + ") #add command=addline when i get it to receive the input from the enteries

nextindex.grid(row=(len(phrasesdb)+1))
newtext.grid(row=(len(phrasesdb)+1), column=1)
newcategory.grid(row=(len(phrasesdb)+1), column=2)
addlinebutton.grid(row=(len(phrasesdb)+1), column=3)

#Root Window draw
rootwindow.mainloop()