import datetime
import subprocess
import pyautogui

def note(text):         # Notiz erstellen
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        subprocess.Popen(["notepad.exe", file_name])


def takeScreenshot():   #Screenshot aufnehmen
    myScreenshot = pyautogui.screenshot()
    save_path = "unknown_faces/test"
    myScreenshot.save(save_path+".jpg")