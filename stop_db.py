import subprocess
import os
import signal

def getPid(name, pstring):
    find_pid_flag = False
    found_start_pid = False
    search_offset = 75
    pid_string = ""
    
    index = pstring.find(name)
    #Begin Search
    if index != -1:
        for i in range(index-search_offset,index):
            if pstring[i] == '\n':
                find_pid_flag = True
            if find_pid_flag:     
                tmp_num = ord(pstring[i])
                if tmp_num >= 48 and tmp_num <= 58:
                    pid_string = pid_string + pstring[i]
                    found_start_pid = True
                else:
                    if found_start_pid:
                        pid = int(pid_string)
                        print("Name: {} PID: {}".format(name,pid))
                        return pid
    print("Name: {} PID: NOT FOUND".format(name))
    return -1
    
#Process search
base_path = "python -u /home/bmernax30/Documents/ddg_rest/"
venv_base_path = "/home/bmernax30/Documents/ddg_rest/"
app_name ="app.py"

course_app = base_path + "course/" + app_name
dungeon_app = base_path + "dungeon/" + app_name
encounter_app = base_path + "encounter/" + app_name
game_app = base_path + "game/" + app_name
hole_app = base_path + "hole/" + app_name
hole_played_app = base_path + "hole_played/" + app_name
player_app = base_path + "player/" + app_name
user_app = base_path + "user/" + app_name

course_venv = venv_base_path + "course/course_env"
dungeon_venv = venv_base_path + "dungeon/dungeon_venv"
encounter_venv = venv_base_path + "encounter/encounter_env"
game_venv = venv_base_path + "game/game_env"
hole_venv = venv_base_path + "hole/hole_env"
hole_played_venv = venv_base_path + "hole_played/hole_played_venv"
player_venv = venv_base_path + "player/player_venv"
user_venv = venv_base_path + "user/user_env"

#Variables
process_string = ""

result = subprocess.run(
    ["ps","-aef"],
    capture_output = True,
    text = True
)
process_string = result.stdout

#Kill The apps
pid = getPid(course_app,process_string)
if pid != -1:
    print("Kill CourseDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("CourseDB already dead.")
    
pid = getPid(dungeon_app,process_string)
if pid != -1:
    print("Kill DungeonDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("DungeonDB already dead.")
    
pid = getPid(encounter_app,process_string)
if pid != -1:
    print("Kill EncounterDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("EncounterDB already dead.")
    
pid = getPid(game_app,process_string)
if pid != -1:
    print("Kill GameDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("GameDB already dead.")
    
pid = getPid(hole_app,process_string)
if pid != -1:
    print("Kill HoleDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("HoleDB already dead.")
    
pid = getPid(hole_played_app,process_string)
if pid != -1:
    print("Kill HolePlayedDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("HolePlayedDB already dead.")
    
pid = getPid(player_app,process_string)
if pid != -1:
    print("Kill PlayerDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("PlayerDB already dead.")
    
pid = getPid(user_app,process_string)
if pid != -1:
    print("Kill UserDB!")
    os.kill(pid, signal.SIGKILL)
else:
    print("UsereDB already dead.")

#Kill The environments
pid = getPid(course_venv,process_string)
if pid != -1:
    print("Kill CourseVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("CourseVENV already dead.")
    
pid = getPid(dungeon_venv,process_string)
if pid != -1:
    print("Kill DungeonVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("DungeonVENV already dead.")
    
pid = getPid(encounter_venv,process_string)
if pid != -1:
    print("Kill EncounterVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("EncounterVENV already dead.")
    
pid = getPid(game_venv,process_string)
if pid != -1:
    print("Kill GameVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("GameVENV already dead.")
    
pid = getPid(hole_venv,process_string)
if pid != -1:
    print("Kill HoleVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("HoleVENV already dead.")
    
pid = getPid(hole_played_venv,process_string)
if pid != -1:
    print("Kill HolePlayedVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("HolePlayedVENV already dead.")
    
pid = getPid(player_venv,process_string)
if pid != -1:
    print("Kill PlayerVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("PlayerVENV already dead.")
    
pid = getPid(user_venv,process_string)
if pid != -1:
    print("Kill UserVENV!")
    os.kill(pid, signal.SIGKILL)
else:
    print("UserVENV already dead.")