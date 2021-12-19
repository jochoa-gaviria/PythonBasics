dayHours = 24
weekDays = 7

weekHours = dayHours*weekDays
print (weekHours)


x=12
y=20
z=1
print (x,y,z)


##Data types##
x=10
y="10"
z=10.1

sum1 = x+x
sum2 = y+y

print (sum1, sum2)
print (type(x), type(y), type(z))
##Data types##


##List types##
studentGrades = [9.1,8.8,7.5] ##this is a list
print (f'Grades of a students: {studentGrades}')
print (f"List of a diferents data types: {[33.1,10, 'a']}")
print (f"A list into a list: {[3.5, 8, 'abc', ['Juan', 'David', 'Ochoa']]}")
##List types##

##Range##
print(f"List of a range: {list(range(1,10))}")
print(f"List of a range incresing by two: {list(range(1,10, 2))}")
##Range##


##Atributes##
#you could use 'dir({datatype})' to see all atributes for a datatypes in python.
# dir(__builtins__)
##Atributes##


##Funtions##
mysum = sum(studentGrades)
length = len(studentGrades)
mean = mysum / length
print (f'the mean value is: {mean}')
##Funtions##


##Exercise - Calculate maximum##
studentGrades = [9.1, 8.8, 7.5]
max_value = max(studentGrades)
print(f'The maximum grade is: {max_value}')
##Exercise - Calculate maximum##


##Exercise - count values##
studentGrades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(f'the total of students with a grade of 10.0 is: {studentGrades.count(10.0)}')
##Exercise - count values##

##Exercise - lowerCase letters##
username="Python3"
print(f'{username} in lower case is: {username.lower()}')
##Exercise - lowerCase letters##



##Dictionaries##
modayTemperature = [9.1, 8.8, 7.5]
studentGrades = {"Marry":9.1, "Sim": 8.8, "John": 7.5}
max_value = max(studentGrades.values())
names = studentGrades.keys()
print(f'The maximum grade of a dictionary is: {max_value}')
##Dictionaries##

##Tuples##
mondayTemperature=(9.1,8.8)
print (f'This is a tuple: {mondayTemperature}')
##you cannot add values to an tuple. 
##Tuples##


##A dictionary with tuples##
day_temperatures = {"morning": (38.4,36.0,37.3), "noon": (35.4,34.6,34.0), "evening": (31.0,32.1,30.8)}
print(f'A dictionary with tuples {day_temperatures}')
##A dictionary with tuples##

##