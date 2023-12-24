import sqlite3

#Table Parameters
conn = sqlite3.connect("games.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"finished INTEGER",
	"course_id INTEGER",
	"game_mode INTEGER",
	"date VARCHAR",
	"num_players INTEGER",
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
	"1,0,1,1,'12/25/23 00:00:00',2,1,2,0,0,0,0,0,0"
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

