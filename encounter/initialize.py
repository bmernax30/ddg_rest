import sqlite3

#Table Parameters
conn = sqlite3.connect("/home/bmernax30/Documents/ddg_rest/encounter/encounters.db")
columns = [
	"id INTEGER PRIMARY KEY",
 	"encounter_challenge VARCHAR",
	"encounter_description VARCHAR",
 	"encounter_pool INTEGER",
	"encounter_image VARCHAR",
	"encounter_name VARCHAR",
	"encounter_type INTEGER",
	"encounter_star INTEGER",
	"encounter_reward_code INTEGER",
	]
#Initialize Data
encounters = [
	"1,'challenge','description',0,'mrt','name',0,0,0",
	"2,'Scoober Putt','You caught yourself in a very thorny plant.',2,'mrt1','Bush of Snare',1,1,2",
	"3,'Scoober Putt','You caught yourself in a very thorny plant.',2,'mrt1','Bush of Snare',1,2,3",
	"4,'Scoober Putt','You caught yourself in a very thorny plant.',2,'mrt1','Bush of Snare',1,3,4",
	"5,'Off Hand Throw','You look into an enchanting mirror and cant tell right from left',2,'mrt2','Elemental Mirror',1,1,2",
	"6,'Off Hand Throw','You look into an enchanting mirror and cant tell right from left',2,'mrt2','Elemental Mirror',1,2,3",
	"7,'Off Hand Throw','You look into an enchanting mirror and cant tell right from left',2,'mrt2','Elemental Mirror',1,3,4",
	"8,'Off Hand Putt','Eww, why did you touch that!?!',2,'mrt3','Gelatinous Cube',1,1,2",
	"9,'Off Hand Putt','Eww, why did you touch that!?!',2,'mrt3','Gelatinous Cube',1,2,3",
	"10,'Off Hand Putt','Eww, why did you touch that!?!',2,'mrt3','Gelatinous Cube',1,3,4",
	"11,'Reverse 3 Steps','Billie Jean is your lover as you moonwalk spontaneously.',2,'mrt4','Ghost of Billie',1,1,2",
	"12,'Reverse 3 Steps','Billie Jean is your lover as you moonwalk spontaneously.',2,'mrt4','Ghost of Billie',1,2,3",
	"13,'Reverse 3 Steps','Billie Jean is your lover as you moonwalk spontaneously.',2,'mrt4','Ghost of Billie',1,3,4",
	"14,'Stand Stills Only','You ignored the sign, Wet Cement',1,'mrt5','Cement Entanglement',1,1,1",
	"15,'Stand Stills Only','You ignored the sign, Wet Cement',1,'mrt5','Cement Entanglement',1,2,2",
	"16,'Stand Stills Only','You ignored the sign, Wet Cement',1,'mrt5','Cement Entanglement',1,3,3",
	"17,'Twice or Its Luck','Nice putt, now do it again. says the Leprachaun holding your disc.',2,'mrt6','Skillcheck Leprechaun',1,1,2",
	"18,'Twice or Its Luck','Nice putt, now do it again. says the Leprachaun holding your disc.',2,'mrt6','Skillcheck Leprechaun',1,2,3",
	"19,'Twice or Its Luck','Nice putt, now do it again. says the Leprachaun holding your disc.',2,'mrt6','Skillcheck Leprechaun',1,3,4",
	"20,'Bag on Putt','You love your discs so much you dont want to leave them.',1,'mrt7','Collectors Abyss',1,1,1",
	"21,'Bag on Putt','You love your discs so much you dont want to leave them.',1,'mrt7','Collectors Abyss',1,2,2",
	"22,'Bag on Putt','You love your discs so much you dont want to leave them.',1,'mrt7','Collectors Abyss',1,3,3",
	"23,'Overhead or Roller','This devious imp named Ty does things a little strange.',1,'mrt8','Informal Imp',1,1,1",
	"24,'Overhead or Roller','This devious imp named Ty does things a little strange.',1,'mrt8','Informal Imp',1,2,2",
	"25,'Overhead or Roller','This devious imp named Ty does things a little strange.',1,'mrt8','Informal Imp',1,3,3",
	"26,'Upside Down putt/throw','A goblin with legs for arms infects your disc.',1,'mrt9','Inverted Goblin',1,1,1",
	"27,'Upside Down putt/throw','A goblin with legs for arms infects your disc.',1,'mrt9','Inverted Goblin',1,2,2",
	"28,'Upside Down putt/throw','A goblin with legs for arms infects your disc.',1,'mrt9','Inverted Goblin',1,3,3",
	"29,'No Challenge','You notice you stepped in some slime and it stained your Idios.',1,'mrt10','Lvl 1 Slime',1,1,1",
	"30,'No Challenge','You notice you stepped in some slime and it stained your Idios.',1,'mrt10','Lvl 1 Slime',1,2,2",
	"31,'No Challenge','You notice you stepped in some slime and it stained your Idios.',1,'mrt10','Lvl 1 Slime',1,3,3",
	"32,'No Backhand outside C3','The walls feel like they are closing in, you have little room to move.',2,'mrt11','Room of Restriction',2,1,2",
	"33,'No Backhand outside C3','The walls feel like they are closing in, you have little room to move.',2,'mrt11','Room of Restriction',2,2,3",
	"34,'No Backhand outside C3','The walls feel like they are closing in, you have little room to move.',2,'mrt11','Room of Restriction',2,3,4",
	"35,'No Forehand outside C3','You cant do that here.',2,'mrt12','Room of Limitation',2,1,2",
	"36,'No Forehand outside C3','You cant do that here.',2,'mrt12','Room of Limitation',2,2,3",
	"37,'No Forehand outside C3','You cant do that here.',2,'mrt12','Room of Limitation',2,3,4",
	"38,'Fairway or C3-C1 or Hazard','You feel entranced and grab a disc. Did you make that decision?',2,'mrt13','Room of Control',2,1,2",
	"39,'Fairway orC3-C1 or Hazard','You feel entranced and grab a disc. Did you make that decision?',2,'mrt13','Room of Control',2,2,3",
	"40,'Fairway or C3-C1 or Hazard','You feel entranced and grab a disc. Did you make that decision?',2,'mrt13','Room of Control',2,3,4",
	"41,'No Passive','The glow fades from you and makes you powerless.',1,'mrt14','Room of Mediocrity',2,1,1",
	"42,'No Passive','The glow fades from you and makes you powerless.',1,'mrt14','Room of Mediocrity',2,2,2",
	"43,'No Passive','The glow fades from you and makes you powerless.',1,'mrt14','Room of Mediocrity',2,3,3",
	"44,'5 to 9 Speed Only','Its dry, so dry. Some of your discs needs a drink of water.',1,'mrt15','Desert Biome',2,1,1",
	"45,'5 to 9 Speed Only','Its dry, so dry. Some of your discs needs a drink of water.',1,'mrt15','Desert Biome',2,2,2",
	"46,'5 to 9 Speed Only','Its dry, so dry. Some of your discs needs a drink of water.',1,'mrt15','Desert Biome',2,3,3",
	"47,'10 Speed or Up Only','Ice skates appear on your feet. You can skate, but you cant stop.',2,'mrt16','Ice Biome',2,1,2",
	"48,'10 Speed or Up Only','Ice skates appear on your feet. You can skate, but you cant stop.',2,'mrt16','Ice Biome',2,2,3",
	"49,'10 Speed or Up Only','Ice skates appear on your feet. You can skate, but you cant stop.',2,'mrt16','Ice Biome',2,3,4",
	"50,'4 Speed or Down Only','Sticky and slow just like the discs you can throw.',1,'mrt17','Swamp Biome',2,1,1",
	"51,'4 Speed or Down Only','Sticky and slow just like the discs you can throw.',1,'mrt17','Swamp Biome',2,2,2",
	"52,'4 Speed or Down Only','Sticky and slow just like the discs you can throw.',1,'mrt17','Swamp Biome',2,3,3",
	"53,'None','Theres nothing here….',1,'mrt18','Empty Room',2,1,1",
	"54,'None','Theres nothing here….',1,'mrt18','Empty Room',2,2,2",
	"55,'None','Theres nothing here….',1,'mrt18','Empty Room',2,3,3",
	"56,'1 Disc','HELLO, Hello, hello, hell.',2,'mrt19','Room of Isolation',2,1,2",
	"57,'1 Disc','HELLO, Hello, hello, hell.',2,'mrt19','Room of Isolation',2,2,3",
	"58,'1 Disc','HELLO, Hello, hello, hell.',2,'mrt19','Room of Isolation',2,3,4",
	"59,'Staff of Retrieval','Some call it just a stick, some call it a life saver',3,'mrt20','Treasure Chest Epic',3,1,1",
	"60,'Staff of Retrieval','Some call it just a stick, some call it a life saver',3,'mrt20','Treasure Chest Epic',3,2,2",
	"61,'Staff of Retrieval','Some call it just a stick, some call it a life saver',3,'mrt20','Treasure Chest Epic',3,3,3",
	"62,'Liquid Luck','Potion that has the main ingrediants of Myrrh and Sodium (Na). More commonly known as Myrrh Na luck.',3,'mrt21','Treasure Chest Legendary',3,1,2",
	"63,'Liquid Luck','Potion that has the main ingrediants of Myrrh and Sodium (Na). More commonly known as Myrrh Na luck.',3,'mrt21','Treasure Chest Legendary',3,2,3",
	"64,'Liquid Luck','Potion that has the main ingrediants of Myrrh and Sodium (Na). More commonly known as Myrrh Na luck.',3,'mrt21','Treasure Chest Legendary',3,3,4",
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

