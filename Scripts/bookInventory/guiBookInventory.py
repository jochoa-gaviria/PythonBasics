from tkinter import *
from backendBookInventory import Database 

bi=Database()

class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Book Store")
        self.titleLabel = Label(window, text="Book Title")
        self.titleLabel.grid(row=1, column=0)
        self.titleValue = StringVar()
        self.titleInput = Entry(window, textvariable=self.titleValue)
        self.titleInput.grid(row=1, column=1)

        self.authorLabel = Label(window, text="Book Author")
        self.authorLabel.grid(row=1, column=2)
        self.authorValue = StringVar()
        self.authorInput = Entry(window, textvariable=self.authorValue)
        self.authorInput.grid(row=1, column=3)

        self.yearLabel = Label(window, text="Book Year")
        self.yearLabel.grid(row=2, column=0)
        self.yearValue = StringVar()
        self.yearInput = Entry(window, textvariable=self.yearValue)
        self.yearInput.grid(row=2, column=1)

        self.idLabel = Label(window, text="Book Id")
        self.idLabel.grid(row=2, column=2)
        self.idValue = StringVar()
        self.idInput = Entry(window, textvariable=self.idValue)
        self.idInput.grid(row=2, column=3)

        self.bookList = Listbox(window, height=6, width=35)
        self.bookList.grid(row=3, column=0, rowspan=6, columnspan=2)
        self.scrollbar = Scrollbar(window)
        self.scrollbar.grid(row=3, column=2, rowspan=6)
        self.bookList.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.bookList.yview)

        self.bookList.bind('<<ListboxSelect>>', self.getSelectedRow)

        self.viewButton = Button(window, text="View all", width=15, command=self.viewCommand)
        self.viewButton.grid(row=4, column=3)

        self.searchButton = Button(window, text="Search Entry", width=15, command=self.searchCommand)
        self.searchButton.grid(row=5, column=3)

        self.addButton = Button(window, text="Add Entry", width=15, command=self.addCommand)
        self.addButton.grid(row=6, column=3)

        self.updateButton = Button(window, text="Update", width=15, command=self.updateCommand)
        self.updateButton.grid(row=7, column=3)

        self.deleteButton = Button(window, text="Delete", width=15, command=self.deleteCommand)
        self.deleteButton.grid(row=8, column=3)

        self.closeButton = Button(window, text="Close", width=15, command=self.closeCommand)
        self.closeButton.grid(row=9, column=3)

    def getSelectedRow(self, event):
        try:
            global selectedTuple
            index=self.bookList.curselection()[0]
            selectedTuple = self.bookList.get(index)
            
            self.titleInput.delete(0,END)
            self.titleInput.insert(END, selectedTuple[1])
            self.authorInput.delete(0,END)
            self.authorInput.insert(END, selectedTuple[2])
            self.yearInput.delete(0,END)
            self.yearInput.insert(END, selectedTuple[3])
            self.idInput.delete(0,END)
            self.idInput.insert(END, selectedTuple[4])
        except IndexError:
            pass

    def viewCommand(self):
        self.bookList.delete(0, END)
        for row in bi.viewAll():
            self.bookList.insert(END, row)

    def searchCommand(self):
        try:
            title = self.titleValue.get()
            author = self.authorValue.get()
            if self.yearValue.get() != '':
                year = int(self.yearValue.get())
            else:
                year = None
            if self.idValue.get() != '':
                bookId = int(self.idValue.get())
            else:
                bookId = None

            self.bookList.delete(0, END)
            for row in bi.search(title=title, author=author, year=year, bookId=bookId):
                self.bookList.insert(END, row)

        except:
            print("Some data is incorret")

    def addCommand(self):
        try:
            if self.titleValue.get() != '':
                title = self.titleValue.get()
            else: 
                title=None
            if self.authorValue.get() != '':
                author = self.authorValue.get()
            else: 
                author = None
            if self.yearValue.get() != '':
                year = int(self.yearValue.get())
            else:
                year = None
            if self.idValue.get() != '':
                bookId = int(self.idValue.get())
            else:
                bookId = None

            if title is None or author is None or year is None or bookId is None:
                print ("Completed all entrys")
            else:
                bi.add(title, author, year, bookId)
                self.viewCommand()

        except:
            print("Some data is incorret")

    def updateCommand(self):
        try:
            title = self.titleValue.get()
            author = self.authorValue.get()
            if self.yearValue.get() != '':
                year = int(self.yearValue.get())
            else:
                year = None
            if self.idValue.get() != '':
                bookId = int(self.idValue.get())
            else:
                bookId = None
            
            if title is None or author is None or year is None or bookId is None:
                print ("Completed all entrys")
            else:
                bi.update(selectedTuple[0],title, author, year, bookId)
                self.viewCommand()
        except:
            print("Pls select a tuple")

    def deleteCommand(self):
        try:
            bi.delete(selectedTuple[0])
            self.viewCommand()
        except:
            print("Pls select a tuple")

    def closeCommand(self):
        window.destroy()

   

    

window = Tk()
Window(window)
window.mainloop()


