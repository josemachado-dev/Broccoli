import main

#V Why do I have to do this? V
phrasesDB = main.phrasesDB
add_Line = main.add_Line
add_MultipleLines = main.add_Multiple_Lines
edit_Line = main.edit_Line
#^ Why do I have to do this? ^

# AREA CONTAMINATED BELOW - TESTING GROUNDS

otherDB = []
otherDB.append({"text": "other text", "category": "other text"})
print(otherDB)

add_Line("1","1")
add_Line("2","2")
add_Line("3","3")

for index, item in enumerate(phrasesDB, start=1):
    print(index, item)

print("---------------")

edit_Line(2, "word", "other word")

add_MultipleLines(otherDB)

for index, item in enumerate(phrasesDB, start=1):
    print(index, item)