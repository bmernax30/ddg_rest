import sqlite3

#Table Parameters
conn = sqlite3.connect("/home/bmernax30/Documents/ddg_rest/dungeon/dungeons.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"dungeon_name VARCHAR",
  	"dungeon_difficulty VARCHAR",
    "num_levels INTEGER",
   	"lvl_1 INTEGER",
    "lvl_2 INTEGER",
    "lvl_3 INTEGER",
    "lvl_4 INTEGER",
    "lvl_5 INTEGER",
    "lvl_6 INTEGER",
    "lvl_7 INTEGER",
    "lvl_8 INTEGER",
    "lvl_9 INTEGER",
    "lvl_10 INTEGER",
    "lvl_11 INTEGER",
    "lvl_12 INTEGER",
    "lvl_13 INTEGER",
    "lvl_14 INTEGER",
    "lvl_15 INTEGER",
    "lvl_16 INTEGER",
    "lvl_17 INTEGER",
    "lvl_18 INTEGER",
    "lvl_19 INTEGER",
    "lvl_20 INTEGER",
    "lvl_21 INTEGER",
    "lvl_22 INTEGER",
    "lvl_23 INTEGER",
    "lvl_24 INTEGER",
    "lvl_25 INTEGER",
    "lvl_26 INTEGER",
    "lvl_27 INTEGER",
    "lvl_28 INTEGER",
    "lvl_29 INTEGER",
    "lvl_30 INTEGER",
    "lvl_31 INTEGER",
    "lvl_32 INTEGER",
    "lvl_33 INTEGER",
    "lvl_34 INTEGER",
    "lvl_35 INTEGER",
    "lvl_36 INTEGER",
	]
#Initialize Data
dungeons = [
	"1,'The Killing Caverns','easy',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
]
#Create the database
create_table_cmd = f"CREATE TABLE dungeon ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for dungeon_data in dungeons:
	insert_cmd = f"Insert INTO dungeon VALUES ({dungeon_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM dungeon")

current_dungeons = cur.fetchall()
for dungeon in current_dungeons:
	print(dungeon)

