import sqlite3


ekadashi=sqlite3.connect("ashadi_ekadashi.db")
cursor= ekadashi.cursor()
cursor.execute("DROP TABLE IF EXISTS festival_supplies")
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS festival_supplies (sr_no INTEGER PRIMARY KEY AUTOINCREMENT ,
Item_name TEXT,
Quantity VARCHAR50,
price VARCHAR20)""")


ashadi_ekadashi_list=[
    ('Flaowers' , '1kg ', '50 rs'),
    ('Fruites' , '12(banana)/1kg(mango)', ' 200 rs'),
    ('sabudana', '1.5kg', '150 rs'),

]
cursor.executemany("INSERT INTO festival_supplies (item_name, Quantity, price) VALUES (?,?,?)" ,ashadi_ekadashi_list)

print("=======Ashadi Ekadashi List 2026========")

cursor.execute("SELECT * FROM festival_supplies")
rows=cursor.fetchall()
for row in rows:
    print(row)


ekadashi.commit()
ekadashi.close()