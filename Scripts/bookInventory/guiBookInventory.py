from tkinter import *
import backendBookInventory as bi

def getSelectedRow(event):
    try:
        global selectedTuple
        index=bookList.curselection()[0]
        selectedTuple = bookList.get(index)
        
        titleInput.delete(0,END)
        titleInput.insert(END, selectedTuple[1])
        authorInput.delete(0,END)
        authorInput.insert(END, selectedTuple[2])
        yearInput.delete(0,END)
        yearInput.insert(END, selectedTuple[3])
        idInput.delete(0,END)
        idInput.insert(END, selectedTuple[4])
    except IndexError:
        pass

def viewCommand():
    bookList.delete(0, END)
    for row in bi.viewAll():
        bookList.insert(END, row)

def searchCommand():
    try:
        title = titleValue.get()
        author = authorValue.get()
        if yearValue.get() != '':
            year = int(yearValue.get())
        else:
            year = None
        if idValue.get() != '':
            bookId = int(idValue.get())
        else:
            bookId = None

        bookList.delete(0, END)
        for row in bi.search(title=title, author=author, year=year, bookId=bookId):
            bookList.insert(END, row)

    except:
        print("Some data is incorret")

def addCommand():
    try:
        if titleValue.get() != '':
            title = titleValue.get()
        else: 
            title=None
        if authorValue.get() != '':
            author = authorValue.get()
        else: 
            author = None
        if yearValue.get() != '':
            year = int(yearValue.get())
        else:
            year = None
        if idValue.get() != '':
            bookId = int(idValue.get())
        else:
            bookId = None

        if title is None or author is None or year is None or bookId is None:
            print ("Completed all entrys")
        else:
            bi.add(title, author, year, bookId)
            viewCommand()

    except:
        print("Some data is incorret")

def updateCommand():
    try:
        title = titleValue.get()
        author = authorValue.get()
        if yearValue.get() != '':
            year = int(yearValue.get())
        else:
            year = None
        if idValue.get() != '':
            bookId = int(idValue.get())
        else:
            bookId = None
        
        if title is None or author is None or year is None or bookId is None:
            print ("Completed all entrys")
        else:
            bi.update(selectedTuple[0],title, author, year, bookId)
            viewCommand()
    except:
        print("Pls select a tuple")

def deleteCommand():
    try:
        bi.delete(selectedTuple[0])
        viewCommand()
    except:
        print("Pls select a tuple")

def closeCommand():
    window.destroy()

window = Tk()
window.wm_title("Book Store")

titleLabel = Label(window, text="Book Title")
titleLabel.grid(row=1, column=0)
titleValue = StringVar()
titleInput = Entry(window, textvariable=titleValue)
titleInput.grid(row=1, column=1)


authorLabel = Label(window, text="Book Author")
authorLabel.grid(row=1, column=2)
authorValue = StringVar()
authorInput = Entry(window, textvariable=authorValue)
authorInput.grid(row=1, column=3)


yearLabel = Label(window, text="Book Year")
yearLabel.grid(row=2, column=0)
yearValue = StringVar()
yearInput = Entry(window, textvariable=yearValue)
yearInput.grid(row=2, column=1)


idLabel = Label(window, text="Book Id")
idLabel.grid(row=2, column=2)
idValue = StringVar()
idInput = Entry(window, textvariable=idValue)
idInput.grid(row=2, column=3)


bookList = Listbox(window, height=6, width=35)
bookList.grid(row=3, column=0, rowspan=6, columnspan=2)
scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=2, rowspan=6)
bookList.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=bookList.yview)

bookList.bind('<<ListboxSelect>>', getSelectedRow)


viewButton = Button(window, text="View all", width=15, command=viewCommand)
viewButton.grid(row=4, column=3)

searchButton = Button(window, text="Search Entry", width=15, command=searchCommand)
searchButton.grid(row=5, column=3)

addButton = Button(window, text="Add Entry", width=15, command=addCommand)
addButton.grid(row=6, column=3)

updateButton = Button(window, text="Update", width=15, command=updateCommand)
updateButton.grid(row=7, column=3)

deleteButton = Button(window, text="Delete", width=15, command=deleteCommand)
deleteButton.grid(row=8, column=3)

closeButton = Button(window, text="Close", width=15, command=closeCommand)
closeButton.grid(row=9, column=3)

window.mainloop()


