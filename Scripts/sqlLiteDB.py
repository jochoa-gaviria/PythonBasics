import sqlite3
def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute(f"INSERT INTO store VALUES('{item}', {quantity}, {quantity})")
    
    conn.commit()
    conn.close()

# insert('Coffe cup', 11, 5)

def view():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

delete('Water Glass')
print(view())

def update(quantity,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=? WHERE item=?", (quantity,item))
    conn.commit()
    conn.close()

update(item='Coffe cup', quantity=9)
print(view())