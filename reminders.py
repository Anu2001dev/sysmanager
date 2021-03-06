import subprocess
import time

def notify(title: str, msg: str = "",
           icon: str = ""):
    cmd = ['notify-send', title, msg, "-i", icon]
    subprocess.Popen(cmd)
    time.sleep(60 * 30)

notify("Drink Water 🍉", icon="/home/anupama/icons8-water-64.png")
