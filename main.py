from pynput.keyboard import Key, Controller
import pyperclip
import os

while True:
    file1 = open("MyFile.txt", "a")
    qs = input("Enter question:  ")
    a = input("Enter file name: ")
    a = a+".py"
    if(a == 'exit.py' or qs == "exit"):
        break

    b = "python "+a
    keyboard = Controller()
    os.system('cls')
    file2 = 0
    if os.system(b) == 0:
        file2 = open(a, "r")
    pyperclip.copy("")

    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release(Key.ctrl)
    keyboard.release('a')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    a = input()

    if(a == 'p'):
        file1.write("QUESTION:\n")
        file1.write(qs)
        file1.write("\nCODE: \n")
        if file2.mode == 'r':
            file1.write(file2.read())
        file1.write("\nOUTPUT: \n")
        str1 = pyperclip.paste()
        print(str1)
        file1.write("\n".join(str1.splitlines()))
        file1.write("\n\n")
        file2.close()

    file1.close()
