import sqlite3

def connect():
    conn=sqlite3.connect("bookInventory/books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, bookId integer)")
    conn.commit()
    conn.close()


def viewAll():
    conn=sqlite3.connect("bookInventory/books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", bookId=""):
    conn=sqlite3.connect("bookInventory/books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR bookId=?", (title, author, year, bookId))
    rows=cur.fetchall()
    conn.close()
    return rows


def add(title, author, year, bookId):
    conn=sqlite3.connect("bookInventory/books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, bookId))
    conn.commit()
    conn.close()

def update(id, title="", author="", year="", bookId=""):
    conn=sqlite3.connect("bookInventory/books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, bookId=? WHERE id=?", (title, author, year, bookId, id))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("bookInventory/books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()



connect()
# add("the sea", "eri", 2021, 5)
# print(viewAll())
# print(search(year=1920))
# delete(2)
# update(3, "Juan corre", "Eri", 2021, 2)
# print(viewAll())
