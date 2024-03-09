#!/bin/sh
course="course"
encounter="encounter"
game="game"
hole="hole"
hole_played="hole_played"
player="player"
user="user"
dungeon="dungeon"
saved_courses="saved_courses"
saved_games="saved_games"
if [ $1 = $course ];
then
    echo "Delete course.db"
    #Delete course db
    rm /home/bmernax30/Documents/ddg_rest/course/courses.db
    python /home/bmernax30/Documents/ddg_rest/course/initialize.py
fi
if [ $1 = $encounter ];
then
    echo "Delete encounters.db"
    #Delete encounters db
    rm /home/bmernax30/Documents/ddg_rest/encounter/encounters.db
    python /home/bmernax30/Documents/ddg_rest/encounter/initialize.py
fi
if [ $1 = $game ];
then
    echo "Delete game.db"
    #Delete game db
    rm /home/bmernax30/Documents/ddg_rest/game/games.db
    python /home/bmernax30/Documents/ddg_rest/game/initialize.py
fi
if [ $1 = $hole ];
then
    echo "Delete holes.db"
    #Delete hole db
    rm /home/bmernax30/Documents/ddg_rest/hole/holes.db
    python /home/bmernax30/Documents/ddg_rest/hole/initialize.py
fi
if [ $1 = $hole_played ];
then
    echo "Delete hole_played.db"
    #Delete hole played db
    rm /home/bmernax30/Documents/ddg_rest/hole_played/holes_played.db
    nohup python /home/bmernax30/Documents/ddg_rest/hole_played/initialize.py
fi
if [ $1 = $player ];
then
    echo "Delete player.db"
    #Delete player db
    rm /home/bmernax30/Documents/ddg_rest/player/players.db
    python /home/bmernax30/Documents/ddg_rest/player/initialize.py
fi
if [ $1 = $user ];
then
    echo "Delete user.db"
    #Delete user db
    rm /home/bmernax30/Documents/ddg_rest/user/users.db
    nohup python /home/bmernax30/Documents/ddg_rest/user/initialize.py
fi
if [ $1 = $dungeon ];
then
    echo "Delete dungeon.db"
    #Delete dungeon db
    rm /home/bmernax30/Documents/ddg_rest/dungeon/dungeons.db
    nohup python /home/bmernax30/Documents/ddg_rest/dungeon/initialize.py
fi
if [ $1 = $saved_games ];
then
    echo "Delete game.db"
    #Delete game db
    rm /home/bmernax30/Documents/ddg_rest/game/games.db
    python /home/bmernax30/Documents/ddg_rest/game/initialize.py

    echo "Delete player.db"
    #Delete player db
    rm /home/bmernax30/Documents/ddg_rest/player/players.db
    python /home/bmernax30/Documents/ddg_rest/player/initialize.py

    echo "Delete hole_played.db"
    #Delete hole played db
    rm /home/bmernax30/Documents/ddg_rest/hole_played/holes_played.db
    python /home/bmernax30/Documents/ddg_rest/hole_played/initialize.py

    echo "Delete dungeon.db"
    #Delete dungeon db
    rm /home/bmernax30/Documents/ddg_rest/dungeon/dungeons.db
    python /home/bmernax30/Documents/ddg_rest/dungeon/initialize.py
fi
if [ $1 = $saved_courses ];
then
    echo "Delete course.db"
    #Delete course db
    rm /home/bmernax30/Documents/ddg_rest/course/courses.db
    python /home/bmernax30/Documents/ddg_rest/course/initialize.py

    echo "Delete hole.db"
    #Delete hole db
    rm /home/bmernax30/Documents/ddg_rest/hole/holes.db
    python /home/bmernax30/Documents/ddg_rest/hole/initialize.py
fi