import json
from difflib import get_close_matches

path = 'files/data.json'

with open(path) as jsonFile:
    data = json.load(jsonFile)


def GetDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        closeWord = get_close_matches(word, data.keys(), cutoff=0.8)
        if closeWord:
            userConfirmation = input("Did you mean <%s> instead? Enter Y if yes, or N if no: " % closeWord[0])
            if userConfirmation == 'Y':
                return data[closeWord[0]]      
            elif userConfirmation=='N':
                return "Word doesn't exists" 
            else:
                return "We didn't understand your entry"

        else:
            return "Word doesn't exists"


word = input("Enter word: ")
output = GetDefinition(word)

if isinstance(output, list):
    for item in output:
        print (item)
else:
    print(output)