import sqlite3

#Table Parameters
conn = sqlite3.connect("/home/bmernax30/Documents/ddg_rest/user/users.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"username VARCHAR",
	"password VARCHAR",
	"phone_id VARCHAR",
	"games_played INTEGER",
	]
#Initialize Data
users = [
	"1,'merna','password','random_phone_id',0",
	]
#Create the database
create_table_cmd = f"CREATE TABLE user ({','.join(columns)})"
conn.execute(create_table_cmd)

#Initialize with some data
for user_data in users:
	insert_cmd = f"Insert INTO user VALUES ({user_data})"
	conn.execute(insert_cmd)

conn.commit()

# Grab the Data
cur = conn.cursor()
cur.execute("SELECT * FROM user")

current_users = cur.fetchall()
for user in current_users:
	print(user)

