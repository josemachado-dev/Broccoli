dictionary = set()

def read_dictionary_file():
    global dictionary
    if dictionary:
        return

    with open("words.txt", "r") as f:
            contents = f.read()
    
    dictionary = set(
        word.lower()
        for word in contents.splitlines()
    )

def is_spelled_correctly(word):
    #Return True if spelled correctly; false otherwise
    word = word.lower()
    read_dictionary_file()
    return word in dictionary