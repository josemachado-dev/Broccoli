phrasesDB = []

#Each obj on the list is a full line on the table
#Each line is as follows
#Index | Text  | Category

#Add obj to list
def add_Line(text, category):
    phrasesDB.append({"text": text, "category": category})

#Add all the objs from another list to this list
#Not sure why I would want this, yet. Maybe to allow merging of lists?
def add_Multiple_Lines(list):
    phrasesDB.extend(list)

#Edit obj in list, given it's index
def edit_Line(n, text, category):
    phrasesDB[n].update({"text": text, "category": category})

#Remove obj from list, given it's index
def remove_Line(n):
    phrasesDB.remove(phrasesDB[n])