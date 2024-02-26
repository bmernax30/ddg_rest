import sqlite3

#Table Parameters
conn = sqlite3.connect("holes_played.db")
columns = [
	"id INTEGER PRIMARY KEY",
	"local_id INTEGER",
 	"hole_id INTEGER",
	"strokes INTEGER",
	"passive_used INTEGER",
	"active_used INTEGER",
	"encounter_id INTEGER",
	"encounter_defeated INTEGER",
 	"hole_completed INTEGER",
	]
#Initialize Data
holes_played = ["1,0,0,0,0,0,0,0,0"]
#Create the database
create_table_cmd = f"CREATE TABLE hole_played ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for hole_played_data in holes_played:
	insert_cmd = f"Insert INTO hole_played VALUES ({hole_played_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM hole_played")

current_holes_played = cur.fetchall()
for hole_played in current_holes_played:
	print(hole_played)

