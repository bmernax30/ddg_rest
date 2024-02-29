import sqlite3

#Table Parameters
conn = sqlite3.connect("/home/bmernax30/Documents/ddg_rest/course/courses.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"course_name VARCHAR",
 	"layout_name VARCHAR",
	"par INTEGER",
	"length INTEGER",
 	"num_holes INTEGER",
	"hole1_id INTEGER",
	"hole2_id INTEGER",
	"hole3_id INTEGER",
	"hole4_id INTEGER",
	"hole5_id INTEGER",
	"hole6_id INTEGER",
	"hole7_id INTEGER",
	"hole8_id INTEGER",
	"hole9_id INTEGER",
	"hole10_id INTEGER",
	"hole11_id INTEGER",
	"hole12_id INTEGER",
	"hole13_id INTEGER",
	"hole14_id INTEGER",
	"hole15_id INTEGER",
	"hole16_id INTEGER",
	"hole17_id INTEGER",
	"hole18_id INTEGER",
	"hole19_id INTEGER",
	"hole20_id INTEGER",
	"hole21_id INTEGER",
	"hole22_id INTEGER",
	"hole23_id INTEGER",
	"hole24_id INTEGER",
	"hole25_id INTEGER",
	"hole26_id INTEGER",
	"hole27_id INTEGER",
	"hole28_id INTEGER",
	"hole29_id INTEGER",
	"hole30_id INTEGER",
	"hole31_id INTEGER",
	"hole32_id INTEGER",
	"hole33_id INTEGER",
	"hole34_id INTEGER",
	"hole35_id INTEGER",
	"hole36_id INTEGER",
	]
#Initialize Data
courses = [
	"1,'Chili','Main',58,7214,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
 	"2,'Chili','Red',58,5373,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
  	"3,'North Ponds','Main',27,1894,9,37,38,39,40,41,42,43,44,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
 	"4,'North Ponds','18 Holes',54,3788,18,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
  	"5,'Shadow Pines','Red',62,5410,18,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
 	"6,'Shadow Pines','White',62,7205,18,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
   	"7,'Shadow Pines','Blue',61,8031,18,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
	]
#Check if Table Exists, Drop if it does
#conn.execute("DROP TABLE course")

#Create the database
create_table_cmd = f"CREATE TABLE course ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for course_data in courses:
	insert_cmd = f"Insert INTO course VALUES ({course_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM course")

current_courses = cur.fetchall()
for course in current_courses:
	print(course)

