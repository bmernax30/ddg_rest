import sqlite3

#Table Parameters
conn = sqlite3.connect("/home/bmernax30/Documents/ddg_rest/dungeon/dungeons.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"dungeon_name VARCHAR",
  	"dungeon_difficulty VARCHAR",
   	"lvl_1 INTERGER",
    "lvl_2 INTERGER",
    "lvl_3 INTERGER",
    "lvl_4 INTERGER",
    "lvl_5 INTERGER",
    "lvl_6 INTERGER",
    "lvl_7 INTERGER",
    "lvl_8 INTERGER",
    "lvl_9 INTERGER",
    "lvl_10 INTERGER",
    "lvl_11 INTERGER",
    "lvl_12 INTERGER",
    "lvl_13 INTERGER",
    "lvl_14 INTERGER",
    "lvl_15 INTERGER",
    "lvl_16 INTERGER",
    "lvl_17 INTERGER",
    "lvl_18 INTERGER",
    "lvl_19 INTERGER",
    "lvl_20 INTERGER",
    "lvl_21 INTERGER",
    "lvl_22 INTERGER",
    "lvl_23 INTERGER",
    "lvl_24 INTERGER",
    "lvl_25 INTERGER",
    "lvl_26 INTERGER",
    "lvl_27 INTERGER",
    "lvl_28 INTERGER",
    "lvl_29 INTERGER",
    "lvl_30 INTERGER",
    "lvl_31 INTERGER",
    "lvl_32 INTERGER",
    "lvl_33 INTERGER",
    "lvl_34 INTERGER",
    "lvl_35 INTERGER",
    "lvl_36 INTERGER",
	]
#Initialize Data
dungeons = [
	"1,'The Killing Caverns','easy',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
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

