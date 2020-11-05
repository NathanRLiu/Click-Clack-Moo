from pynput import keyboard
import os,sys
from playsound import playsound

keyMap = {}

def on_press(key):
    if key in keyMap:
        if keyMap[key] == False:
            playsound(os.path.dirname(os.path.realpath(sys.argv[0]))+"/click.mp3",False)
    else:
        playsound(os.path.dirname(os.path.realpath(sys.argv[0]))+"/click.mp3",False)
    keyMap[key] = True
        
def on_release(key):
    keyMap[key] = False

with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
    listener.join()
listener.start()