## Reading text from a file ##
myFile = open('../Files/fruits.txt')
#print(myFile.read()) # Use the cursor and end at end of the file, so it's better to save the content in a variable
content = myFile.read()
myFile.close() ##Close the file to free RAM and file
print (content)

## Reading text from a file ##

## Reading a file using with function ##
with open('../Files/fruits.txt') as myFile2:
    content2 = myFile2.read()  #The close file executes after this identation.

print (f'with open function \n{content2}')
print (content2[:10])
## Reading a file using with function ##


## Writing text to a File ##
#Python3 >> help(open) to see functions of open function
with open('../Files/vegetables.txt', 'w') as myfile:
    myfile.write("Tomato\nCucumer\nOnion")

## Writing text to a File ##


## Excercise - Count character on a file ##
def countCharactersFile (filePath, character):
    with open(filePath) as file:
        content = file.read()
    return (content.count(character))

print(f"the total of o in the file is: {countCharactersFile('../Files/vegetables.txt', 'o')}")
## Excercise - Count character on a file ##


## Excercise - write 'snail' on a file ##
with open('../Files/file.txt', 'w') as file:
    file.write("snail")
## Excercise - write 'snail' on a file ##

## Excercise - read first words of a file and write in another ##
with open('../Files/fruits.txt') as file:
    fruitContent = file.read()
with open('../Files/file.txt', 'w') as file:
    file.write(fruitContent[:17])
## Excercise - read first words of a file and write in another ##


## Open File and write appending to the end of the file ##
with open('../Files/vegetables.txt', 'a+') as file: # posibles modes: r:read, w:write (re-write the file if exists), x:create a write the file (do not re-write), a: open and append at the end of the file, +: open file for reading and writing
    file.write("\nOkra")
    file.seek(0)
    contentVegetables = file.read()
print(contentVegetables)

## Open File and write appending to the end of the file ##

## Excercise - Read and Append ##
with open("../Files/fruits.txt", "r") as file:
    fruits = file.read()
with open("../Files/vegetables.txt", "a") as file:
    file.write(f'\n{fruits}') 
## Excercise - Read and Append ##

## Excercise - Copy n-times ##
with open ('../Files/file.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    for i in range(2):
        file.write(content)
## Excercise - Copy n-times ##