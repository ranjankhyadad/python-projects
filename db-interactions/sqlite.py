import sqlite3

def create_table():
    con = sqlite3.connect ("lite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventory (item TEXT, price FLOAT, quantity INTEGER)")
    con.commit()
    con.close()

def view_table():
    con = sqlite3.connect ("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM inventory")
    rows= cur.fetchall()
    con.close()
    return rows

def insert(item, price, quantity):
    con = sqlite3.connect ("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO inventory VALUES(?,?,?)",(item, price, quantity))
    con.commit()
    con.close() 

def update(price, quantity,item):
    con = sqlite3.connect ("lite.db")
    cur = con.cursor()
    cur.execute("UPDATE inventory SET price = ?, quantity = ? WHERE item = ?",(price, quantity, item))
    # ? ==> % 
    con.commit()
    con.close()

def delete(item):
    con = sqlite3.connect ("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM inventory WHERE item = ?", (item,)) 
    #comma required, else the number ofarguments is taken as 10
    con.commit()
    con.close()        


create_table()
# insert('Book',15,25)
# insert('Pen',7,30)
# update(35,25,'Book')
# delete('Book')
print(view_table())
