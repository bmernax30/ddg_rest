#!/usr/bin/env bash

#Launch Course Database
source /home/bmernax30/Documents/ddg_rest/course/course_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/course/app.py > /home/bmernax30/Documents/ddg_rest/course/course.log &
deactivate
#Launch Encounter Database
source /home/bmernax30/Documents/ddg_rest/encounter/encounter_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/encounter/app.py > /home/bmernax30/Documents/ddg_rest/encounter/encounter.log &
deactivate
#Launch Game Database
source /home/bmernax30/Documents/ddg_rest/game/game_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/game/app.py > /home/bmernax30/Documents/ddg_rest/game/game.log &
deactivate
#Launch Hole Database
source /home/bmernax30/Documents/ddg_rest/hole/hole_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/hole/app.py > /home/bmernax30/Documents/ddg_rest/hole/hole.log &
deactivate
#Launch Hole Played Database
source /home/bmernax30/Documents/ddg_rest/hole_played/hole_played_venv/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/hole_played/app.py > /home/bmernax30/Documents/ddg_rest/hole_played/hole_played.log &
deactivate
#Launch Player Database
source /home/bmernax30/Documents/ddg_rest/player/player_venv/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/player/app.py > /home/bmernax30/Documents/ddg_rest/player/player.log &
deactivate
#Launch User Database
source /home/bmernax30/Documents/ddg_rest/user/user_env/bin/activate
nohup python -u /home/bmernax30/Documents/ddg_rest/user/app.py > /home/bmernax30/Documents/ddg_rest/user/user.log &
deactivate