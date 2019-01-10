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

for course in lst:
    print(course)
# while DBExist

