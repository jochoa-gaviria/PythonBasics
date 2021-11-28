
## List Comprehension basics. ##
temps = [221, 234, 340, 230]

newTemps = [temp / 10 for temp in temps]

print (newTemps)
## List Comprehension basics. ##

## List Comprehensions with if conditional ##
temps = [221, 234, 340, -9999, 230]

newTemps = [temp / 10 for temp in temps if temp != -9999]
print(newTemps)
## List Comprehensions with if conditional ##


## Excersise - List Comprehensions - Only numbers ##
def onlyNumbers(list):
    return [number for number in list if isinstance(number, int)]

print(onlyNumbers([-99, 'NO DATA', 95, 94, 'NO DATA']))
## Excersise - List Comprehensions - Only numbers ##


## Excersise - List Comprehensions - Only positive numbers ##
def onlyPossitiveNumbers(list):
    return [number for number in list if number>0]

print(onlyPossitiveNumbers([-5, 3, -1, 101]))
## Excersise - List Comprehensions - Only positive numbers ##


## List Comprehensions - if else conditional ##
temps = [221, 234, 340, -9999, 230]

newTemps = [temp / 10 if temp != -9999 else 0 for temp in temps ]
print(newTemps)
## List Comprehensions - if else conditional ##



## Excersise - zeros instead a text ##
def zerosInstead(list):
    return [number if isinstance(number, int) else 0 for number in list]

print(zerosInstead([99, 'no data', 95, 94, 'no data']))
## Excersise - zeros instead a text ##


## Excersise - convert and sum up ##
def sumFloat(list):
    return sum([float(number) for number in list])

print (sumFloat(['1.2', '2.6', '3.3']))
## Excersise - convert and sum up ##