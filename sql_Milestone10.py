# import sqlite3

# # 1. Connect to in-memory database
# conn = sqlite3.connect(":memory:")
# cursor = conn.cursor()

# # 2. Create table with a 'role' column for categorical grouping
# cursor.execute("""
# CREATE TABLE indian_cricket_squad (
#     player_name TEXT,
#     role TEXT,
#     matches INTEGER,
#     total_runs INTEGER
# )
# """)

# # 3. Insert player records with distinct roles
# squad_data = [
#     ('Sachin Tendulkar', 'Batsman', 463, 18426),
#     ('Virat Kohli', 'Batsman', 295, 13848),
#     ('Rohit Sharma', 'Batsman', 265, 10709),
#     ('Rahul Dravid', 'Batsman', 344, 10889),
#     ('MS Dhoni', 'Wicket-Keeper', 350, 10773),
#     ('Yuvraj Singh', 'All-Rounder', 304, 8701),
#     ('Kapil Dev', 'All-Rounder', 225, 3783),
#     ('Ravindra Jadeja', 'All-Rounder', 197, 2756)
# ]

# cursor.executemany("""
# INSERT INTO indian_cricket_squad (player_name, role, matches, total_runs)
# VALUES (?, ?, ?, ?)
# """, squad_data)

# conn.commit()

# print("=== 🏏 Indian Cricket Squad Database Ready ===\n")


# cursor.execute("""
# SELECT role, COUNT(*), SUM(total_runs), AVG(total_runs)
# FROM indian_cricket_squad
# GROUP BY role 
# """)

# grouped_results=cursor.fetchall()

# print("ROLE            |  PLAYERS  |  TOTAL RUNS    |  AVG RUNS ")
# print("-" * 50 )

# for row in grouped_results:
#     role_name, player_count , sum_runs , avg_runs = row 
#     print(f"{role_name: <14} | {player_count:<7} | {sum_runs: <10} | {avg_runs:.2f}")

# conn.close()



import sqlite3

cricket = sqlite3.connect("IPL.db")
cursor=cricket.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Mumbai_Indians (
sr_no INTEGER PRIMARY KEY AUTOINCREMENT,
Players_name TEXT,
Runs INTEGER,
Player_type TEXT NOT NULL 
) 
""")



mi_players = [
    ('Rohit Sharma', 5611, 'Batsman'),
    ('Suryakumar Yadav', 3249, 'Batsman'),
    ('Hardik Pandya', 2300, 'All-Rounder'),
    ('Kieron Pollard', 3412, 'All-Rounder'),
    ('Ishan Kishan', 2324, 'Wicket-Keeper'),
    ('Jasprit Bumrah', 60, 'Bowler')
]
cursor.execute("DELETE FROM Mumbai_Indians")
cursor.executemany("""
INSERT INTO Mumbai_Indians (Players_name, Runs, Player_type)
VALUES (?, ?, ?)
""", mi_players)

cricket.commit()
print("Data Inserted Successfully!")

cursor.execute("""
SELECT Player_type, COUNT(*), SUM(Runs)
FROM Mumbai_indians
GROUP BY Player_type
""")


# for row in cursor.fetchall():
#     role, player_count,total_runs=row
#     print(f"Role: {role} | Players: {player_count} | Total Runs: {total_runs}")


cursor.execute("""
SELECT Players_name , AVG(runs), (Player_type)
FROM Mumbai_indians
GROUP BY Players_name
""")

for row in cursor.fetchall():
    players_name, Avg , Player_type=row
    print(f"Players name:- {players_name}  || Average:{Avg}  || Player Type: {Player_type}")