# import sqlite3


# check= sqlite3.connect("inventory.db")
# cursor= check.cursor()

# cursor.execute("DROP TABLE IF EXISTS student_records")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS student_records(
# Sr_no INTEGER PRIMARY KEY AUTOINCREMENT,
# Student_name TEXT NOT NULL,
# Roll_no INTEGER UNIQUE,
# PASSED_Students_MARKS INTEGER CHECK(PASSED_Students_MARKS >=35)
# )
# """)

# print("STUDENTS RECORDS")

# try:
#     cursor.execute("INSERT INTO student_records(Student_name,Roll_no,PASSED_Students_MARKS) VALUES ('Radha', 21 , 80)")
# except sqlite3.IntegrityError as e:
#     print(f"Not Null: {e}")

# try:
#     cursor.execute("INSERT INTO student_records(Student_name,Roll_no,PASSED_Students_MARKS) VALUES ('Ganesh', 22 , 88)")
# except sqlite3.IntegrityError as e:
#     print(f"Unique: {e}")

# try:
#     cursor.execute("INSERT INTO student_records(Student_name,Roll_no,PASSED_Students_MARKS) VALUES ('Madav', 23 , 90)")
# except sqlite3.IntegrityError as e:
#     print(f"Check marks above 34 : {e}")


# print("Record added")


# cursor.execute("SELECT * FROM student_records")
# all_records=cursor.fetchall()

# for list  in all_records:
#     print(list)


# check.commit()


""" Level wise test challenge Easy + medium + hard """

import sqlite3

fitness=sqlite3.connect("fitness_gym.db")

cursor=fitness.cursor()
cursor.execute("DROP TABLE IF EXISTS gym_members")
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS gym_members(
member_id INTEGER PRIMARY KEY AUTOINCREMENT,
member_name TEXT NOT NULL,
membership_no VARCHAR20 UNIQUE,
age INTEGER CHECK(age>=18) )
""")


cursor.execute("INSERT INTO gym_members( member_name, membership_no , age) VALUES ('Rohan', 'GYM-101', 24)")
print("Record added ")

try:
    cursor.execute("INSERT INTO gym_members(membership_no, age) VALUES('GYM-120', 23)")
except sqlite3.IntegrityError as e:
    print(f"member name NOT NULL: {e}")

try:
    cursor.execute("INSERT INTO gym_members(member_name , membership_no, age) VALUES('madav', 'GYM-101', 23)")
except sqlite3.IntegrityError as e:
    print(f"No Dupication in gym_membersL: {e}")


try:
    cursor.execute("INSERT INTO gym_members(member_name , membership_no, age) VALUES('Gajanan', 'GYM-108', 15)")
except sqlite3.IntegrityError as e:
    print(f"member age must be 17+ : {e}")

cursor.execute("SELECT * FROM gym_members")
all_members_list =cursor.fetchall()
for list in all_members_list:
    print(list)
fitness.commit()


