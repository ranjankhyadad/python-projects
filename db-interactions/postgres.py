import psycopg2

def create_table():
    con = psycopg2.connect ("dbname = 'storage' user = 'postgres' password = 'postgres1307' host = 'localhost' port = '5432'")
# Don't use commas to separate the attributes. Also use '' to assign values  
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventory (item TEXT, price FLOAT, quantity INTEGER)")
    con.commit()
    con.close()

def view_table():
    con = psycopg2.connect ("dbname = 'storage' user = 'postgres' password = 'postgres1307' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM inventory")
    rows= cur.fetchall()
    con.close()
    return rows

def insert(item, price, quantity):
    con = psycopg2.connect ("dbname = 'storage' user = 'postgres' password = 'postgres1307' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO inventory VALUES(%s,%s,%s)",(item, price, quantity))
    # cur.execute("INSERT INTO inventory VALUES('%s','%s','%s')" % (item, price, quantity))
    # The above line of code is correct but is prone to sql injection by hackers. Hence, not preferred
    con.commit()
    con.close() 

def update(price, quantity,item):
    con = psycopg2.connect ("dbname = 'storage' user = 'postgres' password = 'postgres1307' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("UPDATE inventory SET price = %s, quantity = %s WHERE item = %s",(price, quantity, item))
    con.commit()
    con.close()

def delete(item):
    con = psycopg2.connect ("dbname = 'storage' user = 'postgres' password = 'postgres1307' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("DELETE FROM inventory WHERE item = %s", (item,))
    con.commit()
    con.close()        


create_table()
# insert('Book',15,25)
# insert('Pen',7,30)
# update(35,25,'Book')
# delete('Book')
print(view_table())
