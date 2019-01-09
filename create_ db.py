import sqlite3
import os
import atexit
import sys

DBExist=os.path.isfile('schedule.db')
if DBExist:
    sys.exit()

else: #not DBExist
	dbcon = sqlite3.connect('schedule.db')
	cursor = dbcon.cursor()

def close_db():
    dbcon.commit()
    cursor.close()
    dbcon.close()
    # os.remove('schedule.db')

atexit.register(close_db)

def create_tables():
    if not DBExist:  # First time creating the database tables.
        cursor.execute(""" CREATE TABLE courses (id INTEGER PRIMARY KEY , course_name TEXT NOT NULL,student TEXT,number_of_students INTEGER
                            NOT NULL,class_id INTEGER REFERENCES classrooms(id),course_length INTEGER NOT NULL""")
        cursor.execute("""CREATE TABLE students (gradeTEXT PRIMARY KEY , count INTEGER NOT NULL)""")
        cursor.execute(""" CREATE TABLE classrooms (ID INTEGER PRIMARY KEY , LOCATION TEXT NOT NULL , current_course_id INTEGER NOT NULL , current_course_time_lef INTEGER NOT NULL)""")


def insert_course(id, course_name, student,number_of_students,class_id,course_length):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?,?,?)", [id, course_name, student,number_of_students,class_id,course_length])

jhjhjhj
with open(sys.argv[1]) as input:
    for line in input:
        line=line.split(',')
        print(line)
        if line[0]=='C':
            insert_course(line[1],line[2].strip(),line[3].strip(),line[4].strip(),line[5].strip(),line[6].strip())





