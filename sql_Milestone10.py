import sqlite3

# 1. Connect to in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# 2. Create table with a 'role' column for categorical grouping
cursor.execute("""
CREATE TABLE indian_cricket_squad (
    player_name TEXT,
    role TEXT,
    matches INTEGER,
    total_runs INTEGER
)
""")

# 3. Insert player records with distinct roles
squad_data = [
    ('Sachin Tendulkar', 'Batsman', 463, 18426),
    ('Virat Kohli', 'Batsman', 295, 13848),
    ('Rohit Sharma', 'Batsman', 265, 10709),
    ('Rahul Dravid', 'Batsman', 344, 10889),
    ('MS Dhoni', 'Wicket-Keeper', 350, 10773),
    ('Yuvraj Singh', 'All-Rounder', 304, 8701),
    ('Kapil Dev', 'All-Rounder', 225, 3783),
    ('Ravindra Jadeja', 'All-Rounder', 197, 2756)
]

cursor.executemany("""
INSERT INTO indian_cricket_squad (player_name, role, matches, total_runs)
VALUES (?, ?, ?, ?)
""", squad_data)

conn.commit()

print("=== 🏏 Indian Cricket Squad Database Ready ===\n")


cursor.execute("""
SELECT role, COUNT(*), SUM(total_runs), AVG(total_runs)
FROM indian_cricket_squad
GROUP BY role 
""")

grouped_results=cursor.fetchall()

print("ROLE             |  PLAYERS  |  TOTAL RUNS    |  AVG RUNS ")
print("-" * 50 )

for row in grouped_results:
    role_name, player_count , sum_runs , avg_runs = row 
    print(f"{role_name: <14} | {player_count:<7} | {sum_runs: <10} | {avg_runs:.2f}")

conn.close()