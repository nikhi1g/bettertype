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

count = 0
Enable_Keyboard_Hotkeys = False
p.PAUSE = 0.0001
p.DARWIN_CATCH_UP_TIME = 0.0001

recorder = ""
last_char = ""
second_to_last_char = ""


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


def add_new_hotkey(streng: str, pressed_btn: str = None, action=None):
    clear()
    copypaste(streng)


def copypaste(streng):
    pyp.copy(str(streng))
    p.hotkey('command', 'v')


def kill_program():
    os.system("kill " + str(os.getpid()))


def clear():
    p.hotkey('left')
    p.hotkey('left')
    p.hotkey('delete')
    p.hotkey('delete')


def get_three_digit_milliseconds():
    global i, diff
    # get first 3 digit milliseconds
    Element_Array = [str(diff)]
    res = [ele.lstrip('0') for ele in Element_Array]
    diff = res[0]
    i = datetime.datetime.now()


def on_press(key): #mainstuffoccurshere
    global recorder, last_char, second_to_last_char, diff, count, Enable_Keyboard_Hotkeys
    if key == keyboard.Key.esc:
        return False
    try:
        # string manipulation
        recorder += str(format(key.char))
        last_char = recorder[-1]
        if len(recorder) > 1:
            second_to_last_char = recorder[-2]
        if len(recorder) % 2 == 0:
            temp_char = recorder[-1]
            recorder = ""
            recorder += temp_char
        get_three_digit_milliseconds()
        # test_print()

        if Enable_Keyboard_Hotkeys:

            if second_to_last_char == last_char and int(diff) < 190:

                if last_char == "9" and int(diff) < 190:
                    clear()
                    copypaste('()')
                    p.hotkey('left')
                elif last_char == "0":
                    clear()
                    strengg = "()"
                    copypaste(strengg)
                    p.hotkey('left')
                    strengg = '""'
                    copypaste(strengg)
                    p.hotkey('left')
                elif last_char == "p":
                    clear()
                    copypaste('print("")')
                    p.hotkey('left')
                    p.hotkey('left')
                elif last_char == "m":
                    clear()
                    copypaste('if __name__ == "__main__":')
                    p.hotkey('enter')
                elif last_char == "x":
                    clear()
                    sleep(1)
                    pid = os.getpid()
                    print(pid)
                    os.system("kill " + str(pid))
                elif last_char == "w":
                    add_new_hotkey("while True:")
                elif last_char == "f":
                    add_new_hotkey("for i in range():")
                    p.hotkey('left')
                    p.hotkey('left')
                elif last_char == "i":
                    add_new_hotkey("if :")
                    p.hotkey('left')
                elif last_char == "e":
                    add_new_hotkey("elif :")
                    p.hotkey('left')
                elif last_char == "r":
                    clear()
                    sleep(0.5)
                    p.hotkey('ctrl', 'shift', 'r')
                    sleep(0.5)
                    p.hotkey('ctrl', 'shift', 'r')

    except Exception as e:

        if key == keyboard.Key.alt:
            Enable_Keyboard_Hotkeys = True
            print('enabled')


        elif key == keyboard.Key.shift_r:
            Enable_Keyboard_Hotkeys = False
            print('disabled')




def test_print():
    global recorder, last_char, second_to_last_char
    print(recorder, "\t" + second_to_last_char, "\t" + last_char)
    if second_to_last_char == last_char:
        print('tripped')

def start_main(): #starts everything
    Thread(target=millitimer).start()
    start_keyboard()


if __name__ == "__main__":
    start_main()


