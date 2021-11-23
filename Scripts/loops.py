
## For: how and why ##
mondayTemperatures = [9.1, 8.8, 7.5]

# print(round(mondayTemperatures[0]))
# print(round(mondayTemperatures[1]))
# print(round(mondayTemperatures[2]))
print('\nTemperature')
for temperature in mondayTemperatures:
    print(round(temperature))
print('\nLetter')
for letter in 'hello':
    print(letter.title())
## For: how and why ##


## Exercise - loop over colors ##
print('\nLoop over colors')
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)
## Exercise - loop over colors ##


## Exercise - loop over big colors ##
print('\nLoop over big colors')
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color>50:
        print(color)
## Exercise - loop over big colors ##


## Exercise - loop over integer colors ##
print('\nLoop over integer colors')
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int): 
    #if type(color) == int:
        print(color)
## Exercise - loop over integer colors ##


## Exercise - loop over integer and big colors ##
print('\nLoop over integer and big colors')
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)
## Exercise - loop over integer and big colors ##



## Loops over a dictionaries ##
studentGrades = {"Marry":9.1, "Sim":8.8, "John": 7.5}
print('\nDictionary items')
for student in studentGrades.items():
    print (student)

print('\nDictionary keys')
for student in studentGrades.keys():
    print (student)

print('\nDictionary values')
for student in studentGrades.values():
    print (student)
## Loops over a dictionaries ##


## Dictionaries loops and String formatting ##
phone_numbers = {"John Smith": "+573117437028", "Marry Simp": "+573012200690"}

print('\nDictionary String Formatting')
for key, value in phone_numbers.items():
    print("{} has a phone number {}".format(key, value))
print('\n')
for pair in phone_numbers.items():
    print("{} has a phone number {}".format(pair[0], pair[1]))
## Dictionaries loops and String formatting ##



## Excersice - Loop over dictionary and format ##
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
print('\nExcercise - loop over dictionary and format string')
for name, phone in phone_numbers.items():
    print("{}: {}".format(name, phone))
    
## Excersice - Loop over dictionary and format ##


## Excersice -- Loop over dictionary and replace ##
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
print('\nExcercise - loop over dictionary and replace')
for phone in phone_numbers.values():
    print(phone.replace('+', '00'))
## Excersice -- Loop over dictionary and replace ##


## While loop example with user input ##
print('\nWhile loop. Username input exampĺe')
username=''
while username != 'pypy':
    username=input(str("Enter username: "))
## While loop example with user input ##