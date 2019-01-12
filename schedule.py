import sqlite3
import os
import sys
import atexit


def close_db():
    cursor.close()
    dbcon.close()


atexit.register(close_db)

DBExist = os.path.isfile('schedule.db')
if not DBExist: #if database was not found exit
    print('DB not found')
    sys.exit()

# database found
dbcon = sqlite3.connect('schedule.db')
cursor = dbcon.cursor()


def create_list_of_tuples(table):
    cursor.execute('SELECT * FROM ' + table)
    return cursor.fetchall()


def print_table(list_of_tuples):
    for item in list_of_tuples:
        print(item)


def print_tables():
    print('courses')
    print_table(create_list_of_tuples('courses'))
    print('students')
    print_table(create_list_of_tuples('students'))
    print('classrooms')
    print_table(create_list_of_tuples('classrooms'))
    print('\n')


# check if there are courses left in the database
def isempty():
    cursor.execute('SELECT * FROM ' + 'courses')
    return len(cursor.fetchall()) == 0


# returns a list of available classes
def get_available_classes():
    cursor.execute('SELECT * FROM classrooms where classrooms.current_course_time_left = 0')
    return cursor.fetchall()


# returns a course with class_id
def get_course(class_id):
    cursor.execute('SELECT * from courses where courses.class_id ={}'.format(class_id))
    return cursor.fetchone()


print_tables()
# main loop
i = 0
while DBExist and not isempty():
    available_classes=get_available_classes()
    if len(available_classes)> 0:   #case 1 = there are available classes
        for class_room in available_classes:
            course_to_assign=get_course(class_room[0])
            print(('({}) {}: {} is schedule to start').format(i,class_room[1],course_to_assign[1]))
            cursor.execute('UPDATE classrooms SET current_course_id={},current_course_time_left={} where ID={}'
                           .format(course_to_assign[0],course_to_assign[5],course_to_assign[4]))
            sql='UPDATE students SET students.count = %d where grade = %s '
            val=(course_to_assign[3],course_to_assign[2])
            cursor.execute(sql,val)
            # cursor.execute('UPDATE students SET students.count= %d where grade=%s' % (count,grade))
            # #cursor.execute('UPDATE students SET students.count = {} where grade ={}'.format(count,grade))
        print_tables()
        i+=1
    break

    #course just finished





