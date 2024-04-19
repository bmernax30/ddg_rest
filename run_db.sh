#!/usr/bin/env bash

#Delete if Running
nohup python -u /home/bmernax30/Documents/ddg_rest/stop_db.py
sleep 0.5

#Launch Course Database
rm /home/bmernax30/Documents/ddg_rest/course/course.log
source /home/bmernax30/Documents/ddg_rest/course/course_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/course/app.py > /home/bmernax30/Documents/ddg_rest/course/course.log &
deactivate
#Launch Encounter Database
rm /home/bmernax30/Documents/ddg_rest/encounter/encounter.log
source /home/bmernax30/Documents/ddg_rest/encounter/encounter_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/encounter/app.py > /home/bmernax30/Documents/ddg_rest/encounter/encounter.log &
deactivate
#Launch Game Database
rm /home/bmernax30/Documents/ddg_rest/game/game.log
source /home/bmernax30/Documents/ddg_rest/game/game_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/game/app.py > /home/bmernax30/Documents/ddg_rest/game/game.log &
deactivate
#Launch Hole Database
rm /home/bmernax30/Documents/ddg_rest/hole/hole.log
source /home/bmernax30/Documents/ddg_rest/hole/hole_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/hole/app.py > /home/bmernax30/Documents/ddg_rest/hole/hole.log &
deactivate
#Launch Hole Played Database
rm /home/bmernax30/Documents/ddg_rest/hole_played/hole_played.log
source /home/bmernax30/Documents/ddg_rest/hole_played/hole_played_venv/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/hole_played/app.py > /home/bmernax30/Documents/ddg_rest/hole_played/hole_played.log &
deactivate
#Launch Player Database
rm /home/bmernax30/Documents/ddg_rest/player/player.log
source /home/bmernax30/Documents/ddg_rest/player/player_venv/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/player/app.py > /home/bmernax30/Documents/ddg_rest/player/player.log &
deactivate
#Launch User Database
rm /home/bmernax30/Documents/ddg_rest/player/player.log
source /home/bmernax30/Documents/ddg_rest/user/user_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/user/app.py > /home/bmernax30/Documents/ddg_rest/user/user.log &
deactivate
#Launch Dungeon Database
rm /home/bmernax30/Documents/ddg_rest/dungeon/dungeon.log
source /home/bmernax30/Documents/ddg_rest/dungeon/dungeon_venv/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/dungeon/app.py > /home/bmernax30/Documents/ddg_rest/dungeon/dungeon.log &
deactivate