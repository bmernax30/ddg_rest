import sqlite3

#Table Parameters
conn = sqlite3.connect("games.db")
columns = [
	"id INTEGER PRIMARY KEY",
	"game_id VARCHAR",
 	"finished INTEGER",
	"course_name VARCHAR",
 	"layout_name VARCHAR",
	"game_mode INTEGER",
 	"active_start INTEGER",
	"date VARCHAR",
	"num_players INTEGER",
	"player1_username VARCHAR",
	"player2_username VARCHAR",
	"player3_username VARCHAR",
	"player4_username VARCHAR",
	"player5_username VARCHAR",
	"player6_username VARCHAR",
	"player7_username VARCHAR",
	"player8_username VARCHAR",
 	"player1_id INTEGER",
   	"player2_id INTEGER",
    "player3_id INTEGER",
    "player4_id INTEGER",
    "player5_id INTEGER",
    "player6_id INTEGER",
    "player7_id INTEGER",
    "player8_id INTEGER",
	]
#Initialize Data
games = [
	"1,'AAAAA',0,'Chili','Main',1,1,'12/25/23 09:00:11',1,'player1','','','','','','','',1,0,0,0,0,0,0,0",
	]

#Create the database
create_table_cmd = f"CREATE TABLE game ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for game_data in games:
	insert_cmd = f"Insert INTO game VALUES ({game_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM game")

current_games = cur.fetchall()
for game in current_games:
	print(game)

