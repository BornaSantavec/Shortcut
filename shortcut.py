import subprocess
import keyboard
import time

def get_key():
    with open("Path.txt","r") as file:
        line = file.read()
    return line

hotkey = get_key()

while True:
    if keyboard.is_pressed(hotkey):
        subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe'])
        time.sleep(0.05)
    time.sleep(0.01)


#subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe'])
