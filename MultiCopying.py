import msvcrt
import keyboard
import pyperclip

TEXT = str()
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        if key_stroke == b'\x02': #Ctrl + B
            keyboard.send("ctrl + c")

            cur_TEXT = pyperclip.paste()
            TEXT += cur_TEXT
            pyperclip.copy(TEXT)
        else:
            print("Press again")
