import sqlite3

contrustion=sqlite3.connect("contruction_inverntory.db")
cursor=contrustion.cursor()

cursor.execute("DROP TABLE IF EXISTS materials ")
cursor.execute("""
CREATE TABLE IF NOT EXISTS materials(
id  INTEGER PRIMARY KEY AUTOINCREMENT,
item_name TEXT NOT NULL,
category TEXT NOT NULL,
quantity INTEGER CHECK( quantity >=0 ) ,
unit_cost REAL CHECK(unit_cost >=0 )
)
""")

print("TABLE CREATED ")



list = [
    ('CCI OPC', 'Cement', 120, 350.0),
    ('Ultratech PPC', 'Cement', 80, 340.0),
    ('12mm TMT Steel Bar', 'Steel', 5, 62000.0),
    ('Red Bricks', 'Masonry', 5000, 9.0),
    ('River Sand', 'Aggregate', 10, 4500.0),
    ('CPVC Pipe 1 inch', 'Plumbing', 50, 280.0)
]

cursor.execute("DELETE FROM materials")
cursor.executemany(""" INSERT INTO materials(item_name, category,quantity,unit_cost) VALUES (?,?,?,?)""", list)



cursor.execute('SELECT * FROM materials')

print("Material List ")
print(f"--" *50)
list=cursor.fetchall()
for row in list:
    print(row)

cursor.execute("""
SELECT category, COUNT(*), SUM(quantity) , SUM(quantity * unit_cost) 
FROM materials 
GROUP BY category 
""")

print("category summary ")
print(f"="*50)

for row in cursor.fetchall():
    cat_name ,item_count , total_qty, total_rupees=row
    print(f"Category: {cat_name:<10} | Items: {item_count}   | Total QTY : {total_qty :<5} | Total Value : {total_rupees}")