import sqlite3

#Table Parameters
conn = sqlite3.connect("courses.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"course_name VARCHAR",
 	"layout INTEGER",
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
	"1,'Chili',1,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
	]
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

