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


""" Filltering data by using (=, <,>, <=,>=,!=)"""
# import sqlite3

# project=sqlite3.connect("studio.db")

# cursor=project.cursor()

# cursor.execute("DROP TABLE IF EXISTS capcut_project")
# print("dropped")

# cursor.execute(""" CREATE TABLE IF NOT EXISTS capcut_project(Project_id  INTEGER PRIMARY KEY AUTOINCREMENT, Project_name TEXT , Duration_Seconds INTEGER, Status TEXT DEFAULT 'Draft' )""")


# cursor.execute("""INSERT INTO capcut_project(Project_name , Duration_seconds, Status) VALUES ("Beggining of Contruction ", 30 , "Posted" ) """)

# cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds) VALUES ("Bhoomi poojan", 40)""")  


# # cursor.close()
# cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds, Status) VALUES ("DEMOLUSTION WORK", 25, "Posted" )""")

# cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds) VALUES ("Basement Work", 45)""")  

# cursor.execute(""" INSERT INTO capcut_project(Project_name, Duration_seconds) VALUES ("Grondfloor mission started ", 50)""")  

# project.commit()

# print("Records added")


# cursor.execute("SELECT * FROM capcut_project")

# all_records=cursor.fetchall()

# # for capcut_project in all_records:
# #     print(capcut_project)
    
# cursor.execute("SELECT * FROM capcut_project WHERE Duration_seconds >=30")

# morethan30=cursor.fetchall()
# # for project in morethan30:
# #     print(project)

# cursor.execute(""" SELECT * FROM capcut_project WHERE Duration_seconds <40 AND Status ='Posted' """)

# fillter2=cursor.fetchall()
# # for project in fillter2:
# #     print(project)

# cursor.execute(""" SELECT * FROM capcut_project WHERE Status !='Posted' """)

# draftpost=cursor.fetchall()
# # for project in draftpost:
# #     print(project)


# cursor.execute(" SELECT * FROM capcut_project ORDER BY Project_id DESC")

# Descending_order=cursor.fetchall()
# # for project in Descending_order:
# #     print(project)

# cursor.execute(" SELECT * FROM capcut_project ORDER BY Duration_seconds DESC")
# Descending_Duration_time =cursor.fetchall()
# for project in Descending_Duration_time:
#     print(project)
# cursor.close()

""" LIKE Operator ( %TEXT, TEXT% , %TEXT% )"""

import sqlite3

contruction=sqlite3.connect("inverntory.db")

cursor= contruction.cursor()

cursor.execute("DROP TABLE IF EXISTS materials ")

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS materials (
    Item_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Item_name TEXT, 
    Quantity INTEGER,
    Status TEXT DEFAULT 'Pending'
)
""")

cursor.execute("""INSERT INTO materials(Item_name, Quantity)VALUES ("Ultratech Cement", 150)""")

cursor.execute(""" INSERT INTO materials (Item_name, Quantity,Status)
VALUES ("TMT Steal Bars", 5, "Verified")""")

cursor.execute("""INSERT INTO materials(Item_name, Quantity)VALUES ("Ambuja Cement Special ", 80)""")

cursor.execute(""" INSERT INTO materials (Item_name, Quantity,Status)
VALUES ("crush stone ", 12, "Verified")""")
print("Records added ")

contruction.commit()

cursor.execute("SELECT * FROM materials")
all_records=cursor.fetchall()
# for contruction in all_records:
#     print(contruction)


cursor.execute("SELECT * FROM materials WHERE item_name LIKE '%Cement%' ")

cement_only=cursor.fetchall()
# for contruction in cement_only:
#     print(contruction)

cursor.execute("SELECT * FROM materials WHERE Status LIKE 'Verified%' ")

verifed_material=cursor.fetchall()
for contruction in verifed_material:
    print(contruction)



""" Modifying Data Safely (UPDATE & SET with the Golden Rule of WHERE) """

cursor.execute("UPDATE materials SET Status='Verified' WHERE Item_id=1")

print("updated")


cursor.execute("UPDATE materials SET Quantity=25 , Item_name='Crushed Stone Aggregate' WHERE Item_id=4")

print("item no 4 updated ")
cursor.close()



##- [/] Milestone 6: Removing Records (DELETE FROM)
    #- Note: Re-established PC setup; ready to resume coding with fresh energy tomorrow.