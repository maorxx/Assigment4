import sqlite3 	# importing the sqlite3 library will result in a sqlite3 variable
import os 		# os.path.isfile()
import atexit
import sys


DBExist = os.path.isfile('schedule.db')
while DBExist: #need to check if courses is empty

