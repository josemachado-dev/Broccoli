phrasesdb = []

#Each obj on the list is a full line on the table
#Each line is as follows
#Index | Text  | Category

#Add obj to list
def addline(text, category):
    phrasesdb.append({"text": text, "category": category})

#Add all the objs from another list to this list
#Not sure why I would want this, yet. Maybe to allow merging of lists?
def addmultiple(list):
    phrasesdb.extend(list)

#Edit obj in list, given it's index
def editline(n, text, category):
    phrasesdb[n].update({"text": text, "category": category})

#Remove obj from list, given it's index
def removeline(n):
    phrasesdb.remove(phrasesdb[n])
