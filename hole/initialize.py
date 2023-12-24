import sqlite3

#Table Parameters
conn = sqlite3.connect("holes.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"course_id INTEGER",
	"hole_number INTEGER",
	"hole_par INTEGER",
	"hole_distance INTEGER",
	]
#Initialize Data
hole = [
	"1,1,1,3,323"
	]
#Create the database
create_table_cmd = f"CREATE TABLE hole ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for hole_data in hole:
	insert_cmd = f"Insert INTO hole VALUES ({hole_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM hole")

current_holes = cur.fetchall()
for hole in current_holes:
	print(hole)

