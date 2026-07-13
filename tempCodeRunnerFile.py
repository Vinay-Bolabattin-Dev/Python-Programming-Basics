# Database Foundations initialized. SQL for structure, NoSQL for flexibility.


#Main focus on MSc admission work. Standing by for SQLite implementation.


#standing by for SQLite implementation. Conceptual notes locked in.

import sqlite3

conn=sqlite3.connect("studio.db")
cursor=conn.cursor()


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS student( student_name TEXT ,
# Roll_no INTEGER PRIMARY KEY AUTOINCREMENT ) """)# CURD:- C= Creating table named student 

# cursor.execute("""INSERT INTO student(student_name, Roll_no) VALUES ('vittal', 25)""")

# conn.commit
# conn.close
# print("Row data inserted successfully")


# cursor.execute("SELECT * FROM student ") # CURD :- R= selecting /reading data from studio.db file/ database

# all_student=cursor.fetchall()

# print("-----current data of student-----")
# for student in all_student:
#     print(student)




# cursor.execute("UPDATE student SET Roll_no = 50 WHERE student_name = 'vittal' ") # CURD:- U=Updating Roll_no 25 to 50

# cursor.execute("SELECT * FROM student ")

# all_student=cursor.fetchall()

# print("-----current data of student-----")
# for student in all_student:
#     print(student)



# conn.commit()

# print("Row data updated successfully")


# cursor.execute("DELETE FROM student WHERE student_name='vittal' ")#CURD:- D=Deleting student data 

# conn.commit()

# cursor.execute("SELECT * FROM student  ")
# all_student=cursor.fetchall()

# for student in all_student:
#     print(student)

# print("Data removed successfully ")
# conn.close()


import sqlite3

project =sqlite3.connect("studio.db")
cursor=project.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS capcut_project (Project_id INTEGER PRIMARY KEY AUTOINCREMENT,
Porject_Name TEXT , Duration_seconds INTEGER , Status TEXT DEFAULT "draft")
""")

cursor.execute(""" INSERT INTO capcut_project ( Project_Name , Duration_seconds , Status ) 
VALUES ('Beggning of Contruction' , 30 , "exported")""") 

cursor.execute("INSERT INTO capcut_project ( Project_Name , Duration_seconds) VALUES ('Bhoomi poojan' , 40 )") 
project.commit()
cursor.close()
project.close()
print("Successfully added records")