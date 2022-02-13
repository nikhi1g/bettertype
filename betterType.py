import pyautogui as p
from pynput import keyboard
from time import sleep
from threading import Thread
import datetime
import pyperclip as pyp
import sys
import os
'''
known bugs
only works after the second try
'''
i = datetime.datetime.now()
diff = 0

p.PAUSE = 0.0001
p.DARWIN_CATCH_UP_TIME = 0.0001

recorder = ""
first_char = ""
last_char = ""

def millitimer():
    global i
    global diff
    i = datetime.datetime.now()
    while True:
        q = datetime.datetime.now()
        diff1 = str(q - i)
        diff2 = diff1[-9:]
        diff3 = diff2[:-3]
        diff = diff3.replace(".", "")

def start_keyboard():
    with keyboard.Listener(on_press=on_press) as listener: listener.join()


def on_press(key):
    global recorder, first_char, last_char, diff, i
    if key == keyboard.Key.esc:
        return False
    try:
        recorder += str(format(key.char))
        if len(recorder) > 2:
            first_char = recorder[-1]
            recorder = ""
            recorder += first_char
            last_char = ""
        if len(recorder) > 1:
            last_char = recorder[1]

        Element_Array = [str(diff)]
        res = [ele.lstrip('0') for ele in Element_Array]
        diff = res[0]
        i = datetime.datetime.now()

        if len(recorder) == 2 and last_char == first_char and int(diff) < 190:
            pass
    except Exception as e:
        print(e, 'in on press')


def test_print():
    print(recorder, "\t" + first_char, "\t" + last_char)
    print(diff)

Thread(target=millitimer).start()
start_keyboard()

