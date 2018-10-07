#Team Sum over Num_Elements: Xiaojie(Aaron) Li, Stefan Tan
#SoftDev1 pd6
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
# build SQL stmt, save as string
command = """
CREATE TABLE students(
    name TEXT,
    age INTEGER,
    id INTEGER)
"""
c.execute(command)    #run SQL statement
num_peeps = 0
# populate sql table for peeps.csv
with open("peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        num_peeps += 1
        command = "INSERT INTO students(name, age, id) VALUES('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");"
        c.execute(command)

# create courses table
command = """
CREATE TABLE courses(
    code TEXT,
    mark INTEGER,
    id INTEGER)
"""
c.execute(command)    #run SQL statement

# populate sql table for courses.csv
with open("courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        command = "INSERT INTO courses(code, mark, id) VALUES('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");"
        c.execute(command)

# create average table
command = """
CREATE TABLE averages(
    name TEXT,
    id INTEGER,
    average REAL)
"""
# get each student's name, id, and grade
c.execute(command)
command = """
SELECT name, students.id, mark FROM students, courses
WHERE students.id = courses.id
"""
c.execute(command)
avg = c.fetchall() # get all student info
# print(avg)
current = avg[0][0] # current student
sum = 0 # sum thus far
count = 0 # count
for i in range(len(avg)):
    if avg[i][0] == current:
        sum += float(avg[i][2])
        count += 1
    else:
        # print(str(sum/count) + " " + avg[i - 1][0])
        command = (avg[i - 1][0], avg[i - 1][1], avg[i - 1][2])
        c.execute("INSERT INTO averages VALUES(?, ?, ?)", command)
        current = avg[i][0]
        sum = float(avg[i][2])
        count = 1
        #==========================================================
        # function to add rows to courses table
def add(code, mark, id):
    commands = (code, mark, id)
    c.execute("INSERT INTO courses VALUES(?, ?, ?)", commands)

# add a few courses to test
add("Poetry", 68, 3)
add("Great Books", 89, 5)
db.commit() #save changes
db.close() #close database
