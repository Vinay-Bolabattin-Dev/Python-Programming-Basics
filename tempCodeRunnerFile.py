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

project=sqlite3.connect("studio.db")

cursor=project.cursor()

cursor.execute("DROP TABLE IF EXISTS capcut_project")
print("dropped")

cursor.execute(""" CREATE TABLE IF NOT EXISTS capcut_project(Project_id  INTEGER PRIMARY KEY AUTOINCREMENT, Project_name TEXT , Duration_Seconds INTEGER, Status TEXT DEFAULT 'Draft' )""")


cursor.execute("""INSERT INTO capcut_project(Project_name , Duration_seconds, Status) VALUES ("Beggining of Contruction ", 30 , "Posted" ) """)

cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds) VALUES ("Bhoomi poojan", 40)""")  


# cursor.close()
cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds, Status) VALUES ("DEMOLUSTION WORK", 25, "Posted" )""")

cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds) VALUES ("Basement Work", 45)""")  

cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds) VALUES ("Grondfloor mission started ", 50)""")  

project.commit()

print("Records added")


cursor.execute("SELECT * FROM capcut_project")

all_records=cursor.fetchall()

# for capcut_project in all_records:
#     print(capcut_project)
    
cursor.execute("SELECT * FROM capcut_project WHERE Duration_seconds >=30")

morethan30=cursor.fetchall()
# for project in morethan30:
#     print(project)

cursor.execute(""" SELECT * FROM capcut_project WHERE Duration_seconds <40 AND Status ='Posted' """)

fillter2=cursor.fetchall()
# for project in fillter2:
#     print(project)

cursor.execute(""" SELECT * FROM capcut_project WHERE Status !='Posted' """)

draftpost=cursor.fetchall()
# for project in draftpost:
#     print(project)


cursor.execute(" SELECT * FROM capcut_project ORDER BY Project_id DESC")

Descending_order=cursor.fetchall()
# for project in Descending_order:
#     print(project)

cursor.execute(" SELECT * FROM capcut_project ORDER BY Duration_seconds DESC")
Descending_Duration_time =cursor.fetchall()
for project in Descending_Duration_time:
    print(project)
cursor.close()
