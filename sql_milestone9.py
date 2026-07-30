import sqlite3

conn = sqlite3.connect("team_india_m9.db")
cursor = conn.cursor()

# Clean slate
cursor.execute("DROP TABLE IF EXISTS odi_batting_stats")

cursor.execute("""
CREATE TABLE IF NOT EXISTS odi_batting_stats (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    matches INTEGER,
    total_runs INTEGER,
    highest_score INTEGER
)
""")

# Sample Indian ODI Batting Data
players = [
    ('Sachin Tendulkar', 463, 18426, 200),
    ('Virat Kohli', 295, 13848, 183),
    ('Rohit Sharma', 265, 10709, 264),
    ('MS Dhoni', 350, 10773, 183),
    ('Rahul Dravid', 344, 10889, 153),
    ('Yuvraj Singh', 304, 8701, 150)
]

cursor.executemany("""
INSERT INTO odi_batting_stats (player_name, matches, total_runs, highest_score)
VALUES (?, ?, ?, ?)
""", players)

conn.commit()

print("=== 🏏 Team India ODI Stats Ready ===")

cursor.execute("SELECT  COUNT(*) FROM odi_batting_stats")


print("TOTAL NUMBER OF PLAYERS ")
total_number_of_players=cursor.fetchall()
for player_no in total_number_of_players:
    print(player_no)

cursor.execute("SELECT SUM(total_runs) FROM odi_batting_stats")
print('TOTAL NUMBER OF RUNS SCORED BY INDIAN BATTER')

total_runs=cursor.fetchall()
for runs in total_runs:
    print(runs)

cursor.execute("SELECT AVG(total_runs) FROM odi_batting_stats")
average_per_batsman=cursor.fetchone()[0]
print(f"AVRAGE PER BATSMAN :{average_per_batsman}")
