## Syntax errors ##
print(1)
int(9)
int (999)
print(2)
#print 3 #it gaves an error, it doesn't have '()'

## Syntax errors ##


## Runtime errors ##
a=1
b="2"
print(int(2.5))
#print(a+b) ## TypeError: unsupported operand type(s) for +: 'int' and 'str'
print (a + float(b))
print (str(a) + b)
#print (c) # NameError: name 'c' is not defined
c=3
print(c)
## Runtime errors ##


## Questions ##
#mydict = ["name": "John", "surname":"Smith"] # SyntaxError
mydict = {"name": "John", "surname":"Smith"}  ## Correct.
print(mydict)


#a=[1,2,3}  ## SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a=[1,2,3] ## Correct.


#print(john)  #NameError: name 'john' is not defined
john = "person"
print(john)

#mylist = [John, Jack, Jim]  ##NameError: name 'John' is not defined
John = "person"
Jack = "person2"
Jim = "person3"
mylist = [John, Jack, Jim]
print(mylist)
## Questions ##



## Fixing errors ##
try:
    c=3
    z = (c/0)
    print (z)
except ZeroDivisionError:
    z=0
    print(z)
    print(ZeroDivisionError)


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ZeroDivisionError
print(divide(1,0))
## Fixing errors ##