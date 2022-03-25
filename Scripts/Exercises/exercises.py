"""
Exercises...


"""
##Counter of a word##
from operator import contains


def counter(word):
    return len(word)

# print(counter("Hello world"))
##Counter of a word##


##Second element of every tuple##

def secondElementTuple():
    elements = (
    (1, 4),
    (4, 5),
    (6, 7),
    (1, 3)
    )

    for element in elements:
        print (element[-1])

# secondElementTuple()
##Second element of every tuple##

##Sum##
def sumPrint(a,b,c):
    print (a+b+c)

# sumPrint(3,4,6)
##Sum##



##Turn a tuple into a dictionary##
def makeDict(tuple):
    dictionary = dict(tuple)
    return dictionary

customer = (
    ('id','98698761'), 
    ('name', 'marry'), 
    ('surname', 'smith'), 
    ('rented_books', 3 )
    )
# print(makeDict(customer))
##Turn a tuple into a dictionary##


##print especific item of a list##

def printItem():
    passwords = ['ccavfb', 'baaded', 'bbaa', 'aaeed', 'vbb', 'aadeba', 'aba', 'dee', 'dade', 'abc', 'aae', 'dded', 'abb', 'aaf', 'ffaec']
    validString = ('ab','ba')
    for password in passwords:
        if any(s in password for s in validString):
            print(password)

# printItem()

##print especific item of a list##


##Anybody in there##
def anybodyInThere(list, obj):
    if not obj in list:
        list.append(obj)
    return list
# print (anybodyInThere(['a',2,'b',3],4))
##Anybody in there##


##Print First element of a list if is an integer##

def printFirstElement():
    elements = [
        [1, 4, 6, 7],
        [4, 5, 6],
        [6, 7, 8],
        [],
        ["nodata", "nodata"],
        [1, 3]
                ]
    for element in elements:
        try:
            if isinstance(element[0], int):
                print(element[0])
        except:
            pass
# printFirstElement()
##Print First element of a list if is an integer##

##Print First element of a list##
def firstItemList(lista):
    return lista[0]
# print(firstItemList(['a',3,6,'bbb']))
##Print First element of a list##

##Print Last element of a list##
def lastItemList(lista):
    return lista[-1]
# print(lastItemList(['a',3,6,'bbb']))
##Print Last element of a list##


##Print first and Last element of a list##
def firstlastItemList(lista):
    return lista[0], lista[-1]
# print(firstlastItemList(['a',3,6,'bbb']))
##Print first and Last element of a list##


##Multiple arguments of a function##
def multipleArgs(*args):
    return [x for x in args]

print(multipleArgs(1,4,5,67,'asss','s'))
##Multiple arguments of a function##



