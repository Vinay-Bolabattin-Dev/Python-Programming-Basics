# import sqlite3

# conn = sqlite3.connect("inventory_m8.db")
# cursor = conn.cursor()

# # Clean slate
# cursor.execute("DROP TABLE IF EXISTS site_inventory")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS site_inventory (
#     item_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     item_name TEXT NOT NULL,
#     quantity INTEGER
# )
# """)

# # Inserting 10 sample records
# items = [
#     ('Cement Bags', 500),
#     ('Steel Rods', 200),
#     ('Sand (Tons)', 50),
#     ('Bricks', 10000),
#     ('Gravel (Tons)', 30),
#     ('Paint Cans', 40),
#     ('Pipes', 150),
#     ('Electrical Wire Spools', 25),
#     ('Safety Helmets', 60),
#     ('Water Tanks', 5)
# ]

# cursor.executemany("INSERT INTO site_inventory (item_name, quantity) VALUES (?, ?)", items)
# conn.commit()

# # print("=== 📦 ALL 10 ITEMS IN DATABASE ===")
# # cursor.execute("SELECT * FROM site_inventory")
# # for row in cursor.fetchall():
# #     print(row)

# ## testing LIMIT AND OFFSET operators 

# cursor.execute("SELECT * FROM site_inventory LIMIT 5")
# top_5_records=cursor.fetchall()

# # print("1st Top 5 records")
# # for top_list in top_5_records:
# #     print(top_list)


# cursor.execute("SELECT * FROM site_inventory WHERE quantity>=100 LIMIT 3 OFFSET 2") 
# high_quantity = cursor.fetchall()
# for list in high_quantity:
#     print(list)
# conn.close()



""" LEVEL WISE CHALLENGE EASY TO HARD """

import sqlite3

cricket= sqlite3.connect("IPL_Teams.db")

cursor=cricket.cursor()


cursor.execute('DROP TABLE IF EXISTS IPL_2026 ')

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS IPL_2026
(team_id INTEGER PRIMARY KEY AUTOINCREMENT,
team_name TEXT NOT NULL ,
points INTEGER CHECK (points >=0 ) )""")

teams_data = [
    ('CSK', 18),
    ('MI', 16),
    ('KKR', 14),
    ('RCB', 14),
    ('RR', 12),
    ('GT', 10),
    ('DC', 8),
    ('PBKS', 6),
    ('SRH', 6),
    ('LSG', 4)
]

cursor.executemany("INSERT INTO IPL_2026 (team_name, points) VALUES (?, ?)", teams_data)

print("DATA ADDED")

cursor.execute("SELECT * FROM IPL_2026")
all_records=cursor.fetchall()
for list in all_records:
    print(list)


print("TOP 4 TEAMS Qulifiers")
cursor.execute("SELECT * FROM IPL_2026 WHERE points>12 LIMIT 4")
qulifiers=cursor.fetchall()
for top_team in qulifiers:
    print(top_team)


print("Less chances of qulifications")
cursor.execute('SELECT * FROM IPL_2026 WHERE points<8 LIMIT 3 OFFSET 1')
bottom2=cursor.fetchall()
for E in bottom2:
    print(E)

cricket.commit()
