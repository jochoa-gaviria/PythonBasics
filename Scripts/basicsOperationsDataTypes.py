
##Exersice - Append item to list##
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)
##Exersice - Append item to list##

##Exersice - remove item from a list##
print("\n")
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)
print(seconds)
##Exersice - remove item from a list##


##Exersice - remove some items from a list##
print("\n")
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)
seconds.remove(1.10001399445)
seconds.remove(1.023458894)
print(seconds)
##Exersice - remove some items from a list##


##Get index of a value from a list##
print("\n")
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
print(f'get a index of a value: {seconds.index(1.2323442655)}')
##Get index of a value from a list##

##Get a value from an index of a list##
print("\n")
print(f'get a value using __getitem__ {seconds.__getitem__(1)}')
print(f'get a value using a index into a [] {seconds[1]}')
##Get a value from an index of a list##

##Exersice - get items of a list##
print("\n")
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])
print(serials[0], serials[2], serials[5])
##Exersice - get items of a list##

##Exersice - Append the first itm of weekend to workdays#
print("\n")
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(f'Work days {workdays}')
##Exersice - Append the first itm of weekend to workdays#

##Accesing list slices##
print("\n")
print(workdays[1:3])
print(workdays[0:2])
print(workdays[:3])
print(workdays[3:])
##Accesing list slices##


##Accesing list slices with negative index##
print("\n")
print(workdays[-2:])
##Accesing list slices with negative index##

##Accesing list slices in strings##
print("\n")
mondayTemperatures = ["hello", 1,2,3]
print(mondayTemperatures[0])
print(mondayTemperatures[0][1])
##Accesing list slices in strings##


##Execise - print out the slice ['b', 'c', 'd'] of the letters list##
print("\n")
letters = ['a','b','c','d','e','f','g']
print(letters[1:4])
##Execise - print out the slice ['b', 'c', 'd'] of the letters list##


##Exercise - print out the slice ['a','b','c'] of the letters list##
print("\n")
print(letters[:3])
##Exercise - print out the slice ['a','b','c'] of the letters list##

##Exercise - print out the slice ['e','f','g'] of the letters list##
print("\n")
print(letters[-3:])
##Exercise - print out the slice ['e','f','g'] of the letters list##


##Accessing items in dictionaries##
print("\n")
studentGrades = {"Marry":9.1, "Sim": 8.8, "John": 7.5}
print(studentGrades["Sim"])
##Accessing items in dictionaries##

##Converting between datatypes##
    #From tuple to list
print("\n")
dataTuple=(1,2,3)
print(f'tuple{dataTuple}')
dataList= list(dataTuple)
print(f'list {dataList}')
    #From list to tuple
dataList=[1,2,3]
print(f' list {dataList}')
dataTuple = tuple(dataList)
print(f' tuple {dataTuple}')
    #From list to dictionary
dataList = [["name", "John"], ["surname", "smith"]]
print(f' list {dataList}')
dataDictionary = dict(dataList)
print(f'dictionary {dataDictionary}')
##Converting between datatypes##