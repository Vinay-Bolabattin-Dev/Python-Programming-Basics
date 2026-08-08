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


cursor.execute("SELECT * FROM materials WHERE quantity < 20 ")

print("=====LOW STOCK (PLEASE ORDER SOON !!)====")
low_stock=cursor.fetchall()
for stock in low_stock:
    print(stock)


cursor.execute("UPDATE materials SET quantity = 20 WHERE id = 3 ")

cursor.execute("UPDATE materials SET quantity=20 WHERE id =5 ")
print("stock updated")


cursor.execute("DELETE FROM materials WHERE id=6")
print("DELETED successfully")



while True:
    print("\n---CONTRUSTION INVENTORY MENU---")
    print("1. view all materials")
    print("2. Add materials ")
    print("3. Category Summary ")
    print("4. Low stock Alert ")
    print("5. Update stock ")
    print("6. Delete material ")
    print("7. Exit ")


    choice =input("\n Enter choice(1-7) ").strip()

    match choice:
        case "1":
            cursor.execute("SELECT * FROM materials ")
            records=cursor.fetchall()
            print("All materials lsit ")
            for row in records:
                print(row)

        case "2":
            print("--Add new material ")
            item_name=input("Enter item name: ")
            category = input("Enter category (Cement/Steel/etc.): ")
            quantity = int(input("Enter quantity: "))
            unit_cost = float(input("Enter unit cost (₹): "))

            cursor.execute("""
              INSERT INTO materials (item_name, category, quantity, unit_cost)
              VALUES (?, ?, ?, ?)
              """, (item_name, category, quantity, unit_cost))
            
            contrustion.commit()  # Saves change permanently to DB file
            print(f"Added {item_name} to database successfully!")

        case "3" :
            cursor.execute("""
            SELECT category, COUNT(*), SUM(quantity), SUM(quantity * unit_cost)
            FROM materials
            GROUP BY category
            """)

            print("category summary ")
            print(f"="*50)

            for row in cursor.fetchall():
                cat_name ,item_count , total_qty, total_rupees=row
                print(f"Category: {cat_name:<10} | Items: {item_count}   | Total QTY : {total_qty :<5} | Total Value : {total_rupees}")


        case "4":
            cursor.execute("SELECT * FROM materials WHERE quantity < 20 ")
            print("=====LOW STOCK (PLEASE ORDER SOON !!)====")

            low_stock=cursor.fetchall()
            for stock in low_stock:
                print(stock)

        case "5":
            print("\n----Update stock Quantity---")
            item_id = int(input("Enter the ID of the material to update: "))
            new_qty=int(input("Enter a new quantity: "))

            cursor.execute("UPDATE materials SET quantity =? WHERE id= ? ", (new_qty ,item_id)) 
            print(f"Stock Updated at ID: {item_id}")

        case "6":
            print("\n Delete material")
            item_id= int(input("Enter the ID of the material to delete: "))

            cursor.execute("DELETE FROM materials WHERE id=?", (item_id))

            contrustion.commit()
            print(f"Enter id {item_id } Deleted Peremanently")
            
        case "7":
            print("\nExiting application. ")
            break

        case _:
            print("Invalid choice! Please enter a number between 1 and 7.")




