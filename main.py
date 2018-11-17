#External libraries
import tkinter as tk

#Each obj on the list is a full line on the table
#Each line is as follows
#Index | Text  | Category
phrasesdb = []

#This serves merly to test new functions, and see if they're being called when they should
def debug(event):
    print("the function is working")


#Add obj to list
def addline():
    ##This creates new obj with values from the input fields, and inserts it in the list
    newobj = {"text": newtext.get(), "category": newcategory.get()}
    phrasesdb.append(newobj)
    
    ##This shows new obj on the table
    newesttext = tk.Label(tableframe, text=newobj["text"])
    newestcategory = tk.Label(tableframe, text=newobj["category"])

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
def editline(n, text, category):
    phrasesdb[n].update({"text": text, "category": category})

#Remove obj from list, given it's index
def removeline(n):
    phrasesdb.remove(phrasesdb[n])


#Definition of root window
rootwindow = tk.Tk()
rootwindow.title("improved-broccoli")


##Table showing content
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


#Root Window draw
rootwindow.mainloop()