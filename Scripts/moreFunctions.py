## Funtion with multiple arguments ##
def area(a, b):
    return a*b

print(f"the area is: {area(4,5)}")
## Funtion with multiple arguments ##



## Excercise - Multiple arguments of a string ##
def strings(text1, text2):
    return (f"{text1}  {text2}")

print(strings("juan", "david"))
## Excercise - Multiple arguments of a string ##


## Default - Non-Default parameters ##
def area(a, b=2): #b=2 is a default parameter
    return a*b

print(f"the area is (Non-Default parameter): {area(4)}") #Is no neccesary to send the value for b variable
## Default - Non-Default parameters ##

## Keyword - Non-Keyword parameters ##
def area(a, b): 
    return a*b

print(f"the area is (Keyword parameter): {area(b=4, a=2)}") #The order doesn't meant 'cause we assined the value for each variable 
## Keyword - Non-Keyword parameters ##


## Indefinite number of arguments ##
def mean(*args):
    return sum(args) / len(args)

print(mean(1,2,3,4,555,8))
## Indefinite number of arguments ##


## Excercise - Average function ##
def average(*args):
    return sum(args)/len(args)

print(average(87,45,21,33,2,1,4))
## Excercise - Average function ##


## Excercise - indefinite number of strings ##
def stringsUpperList(*args):
    args = [x.upper() for x in args] #ListComprehensions
    return sorted(args)

print(stringsUpperList('juan', 'david', 'is', 'learning', 'python'))
## Excercise - indefinite number of strings ##


## Functions with a indefinite numbers of keywords ##
def mean(**kwargs):
    return kwargs

print(mean(a=1, b='juan', c=5))
## Functions with a indefinite numbers of keywords ##


## Excersece - indefinite number of keywords Argument ##
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=5, b=4))
## Excersece - indefinite number of keywords Argument ##