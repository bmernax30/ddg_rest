import sqlite3

#Table Parameters
conn = sqlite3.connect("encounters.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"encounter_pool INTEGER",
	"encounter_image VARCHAR",
	"encounter_name VARCHAR",
	"encounter_type INTEGER",
	"encounter_star INTEGER",
	"encounter_reward_code INTEGER",
	]
#Initialize Data
encounters = [
	"1,0,'mrt1','Bush of Snare',1,1,1"
	]
#Create the database
create_table_cmd = f"CREATE TABLE encounter ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for encounter_data in encounters:
	insert_cmd = f"Insert INTO encounter VALUES ({encounter_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM encounter")

current_encounters = cur.fetchall()
for encounter in current_encounters:
	print(encounter)

