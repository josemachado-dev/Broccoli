import main

#V Why do I have to do this? V
phrasesdb = main.phrasesdb
addline = main.addline
addmultiple = main.addmultiple
editline = main.editline
#^ Why do I have to do this? ^

# AREA CONTAMINATED BELOW - TESTING GROUNDS

otherdb = []
otherdb.append({"text": "other text", "category": "other text"})
print(otherdb)

addline("1","1")
addline("2","2")
addline("3","3")

for index, item in enumerate(phrasesdb, start=1):
    print(index, item)

print("---------------")

editline(2, "word", "other word")

addmultiple(otherdb)

for index, item in enumerate(phrasesdb, start=1):
    print(index, item)