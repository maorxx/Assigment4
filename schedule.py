import sqlite3 	# importing the sqlite3 library will result in a sqlite3 variable
import os 		# os.path.isfile()
import sys

DBExist = os.path.isfile('schedule.db')
if not DBExist:
    print('DB not found')
    sys.exit()

#DB found
dbcon = sqlite3.connect('schedule.db')
cursor = dbcon.cursor()
cursor.execute('SELECT * FROM ' + 'courses')
lst = cursor.fetchall()
num_of_courses=len(lst)

def get_course(class_id):
    cursor.execute('SELECT courses.course_length from courses where courses.class_id =' + class_id)
    course_length = cursor.fetchone()
    return course_length[0]


while DBExist and num_of_courses > 0:
    #class room is free
    cursor.execute('SELECT classrooms.id FROM classrooms where classrooms.current_course_time_left = 0')
    free_classroom_ids = cursor.fetchall()
    for row in free_classroom_ids:
        course_length = get_course(str(row[0]))
        cursor.execute('UPDATE classrooms set current_course_time_left =' + str(course_length) + 'where ID =' + str(row[0]))
        # print(cursor.execute('SELECT classrooms.current_course_time FROM classrooms'))
    break
    #class room is occupied


    #course just finished




