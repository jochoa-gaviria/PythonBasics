def textProcessing(phrase):
    if phrase.startswith(("how", "what", "why")):
        return f"{phrase.capitalize()}?" 
    else:
        return f"{phrase.capitalize()}."


def textInput():
    listText = []
    loopContinue = True
    while loopContinue:
        text=str(input("Say something: "))
        if(text != "\end"):
            listText.append(textProcessing(text))
        else:
            loopContinue = False
    return listText


list=textInput()
print(" ".join(list))



