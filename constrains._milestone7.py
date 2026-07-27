import sqlite3


check= sqlite3.connect("inventory.db")
cursor= check.cursor()

cursor.execute("DROP TABLE IF EXISTS student_records")

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_records(
Sr_no INTEGER PRIMARY KEY AUTOINCREMENT,
Student_name TEXT NOT NULL,
Roll_no INTEGER UNIQUE,
PASSED_Students_MARKS INTEGER CHECK(PASSED_Students_MARKS >=35)
)
""")

print("STUDENTS RECORDS")

try:
    cursor.execute("INSERT INTO student_records(Student_name,Roll_no,PASSED_Students_MARKS) VALUES ('Radha', 21 , 80)")
except sqlite3.IntegrityError as e:
    print(f"Not Null: {e}")

try:
    cursor.execute("INSERT INTO student_records(Student_name,Roll_no,PASSED_Students_MARKS) VALUES ('Ganesh', 22 , 88)")
except sqlite3.IntegrityError as e:
    print(f"Unique: {e}")

try:
    cursor.execute("INSERT INTO student_records(Student_name,Roll_no,PASSED_Students_MARKS) VALUES ('Madav', 23 , 90)")
except sqlite3.IntegrityError as e:
    print(f"Check marks above 34 : {e}")


print("Record added")


cursor.execute("SELECT * FROM student_records")
all_records=cursor.fetchall()

for list  in all_records:
    print(list)


check.commit()