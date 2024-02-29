import sqlite3

#Table Parameters
conn = sqlite3.connect("/home/bmernax30/Documents/ddg_rest/player/players.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"local_id INTEGER",
 	"username VARCHAR",
 	"player_class VARCHAR",
 	"total_holes INTEGER",
  	"holes_played INTEGER",
  	"player_score INTEGER",
  	"player_active INTEGER",
  	"player_stars INTEGER",
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
players = ["1,0,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"]
#Create the database
create_table_cmd = f"CREATE TABLE player ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for player_data in players:
	insert_cmd = f"Insert INTO player VALUES ({player_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM player")

current_players = cur.fetchall()
for player in current_players:
	print(player)

