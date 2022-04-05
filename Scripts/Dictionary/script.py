import json
from difflib import get_close_matches

path = 'files/data.json'

with open(path) as jsonFile:
    data = json.load(jsonFile)


def GetDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        closeWord = get_close_matches(word, data.keys())
        if closeWord:
            return data[closeWord[0]]
        else:
            return "Word doesn't exists"


word = input("Enter word: ")
print(GetDefinition(word))