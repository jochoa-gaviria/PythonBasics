import sqlite3
class Database:

    def __init__(self):  # Constructor
        self.conn=sqlite3.connect("bookInventory/books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, bookId integer)")
        self.conn.commit()


    def viewAll(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        # self.conn.close()
        return rows

    def search(self, title="", author="", year="", bookId=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR bookId=?", (title, author, year, bookId))
        rows=self.cur.fetchall()
        # self.conn.close()
        return rows


    def add(self, title, author, year, bookId):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, bookId))
        self.conn.commit()
        # self.conn.close()

    def update(self, id, title="", author="", year="", bookId=""):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, bookId=? WHERE id=?", (title, author, year, bookId, id))
        self.conn.commit()
        # self.conn.close()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
        # self.conn.close()

    def __del__(self):
        self.conn.close()