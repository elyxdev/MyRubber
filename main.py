from colorama import Fore, init, Back
import pyautogui as pg
import subprocess
import time
import sys
import os


quiet = False # Modo silencioso
valid = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

def jilog(text):
    if not quiet == True:
        print(text)

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def osn():
    if os.name == "nt":
        jilog(f"{Fore.BLUE}[Current OS]> {Fore.RESET} WindowsNT")
    else:
        jilog(f"{Fore.BLUE}[Current OS]> {Fore.RESET} Possible Linux")

def pwd():
    jilog(f"\n{Fore.BLUE}[Current DIR]> {Fore.LIGHTBLUE_EX}")
    if os.name == "nt":
        jilog(subprocess.check_output('cd', shell=True, text=True))
    else:
        jilog(subprocess.check_output('pwd', shell=True, text=True))
    jilog(Fore.RESET)

def vulnus_made():
    jilog(f"""{Fore.CYAN}Yos built this with love <3
          {Fore.RESET}""")

def banner():
    jilog(f"""{Fore.LIGHTBLUE_EX}=================================
{Fore.BLUE}MyRubber - Yos
{Fore.LIGHTBLUE_EX}================================={Fore.RESET}""")

def setup():
    cls()
    vulnus_made()
    pwd()
    time.sleep(2)
    main()

def main(keysfilename="keys.txt"):
    cls()
    banner()
    pwd()
    osn()
    jilog(f"\n{Fore.LIGHTBLUE_EX}[INF]> Trying to read {Fore.LIGHTCYAN_EX}{keysfilename}{Fore.RESET}")
    try:
        f = open(keysfilename, "r")
    except:
        jilog(f"{Fore.LIGHTRED_EX}{keysfilename} not found{Fore.RESET}. Enter keystroke filename...")
        try:
            f = open(input(f"{Fore.CYAN}[FILENAME]> {Fore.RESET}"))
        except:
            jilog(f"{Fore.LIGHTRED_EX}You mistyped{Fore.RESET}. Try again...")
            time.sleep(3)
            main(keysfilename=keysfilename)
    
    for key in f.readlines():
        key = str(key)
        if key[-1::] == "\n":
            key = key[:-1:]
        jilog(f"{Fore.LIGHTCYAN_EX}[KEY]> ({len(key)} / {len(key.split('+'))}) {Fore.RESET}{key} ")

        if key[0:1] == "'":
            key = key[1::]
            pg.write(key,0.01)
            continue
        
        if key[0:1] == "\\":
            if key[1::].split(" ")[0] == "sleep":
                time.sleep(float(key[1::].split(" ")[1]))
                continue
            elif key[1::].split(" ")[0] == "mv":
                pg.moveTo(int(key[1::].split(" ")[1]), int(key[1::].split(" ")[2]))
                continue

        if str(len(key.split("+"))) == "2":
            key = key.split("+")
            pg.hotkey(key[0],key[1])
            continue

        elif str(len(key.split("+"))) > "2":
            key = key.split("+")
            for k in key:
                pg.keyDown(k)
            for k in key:
                pg.keyUp(k)
            continue
        
        elif key == "click" or key == "lclick":
            pg.click(button='left')
            continue

        elif key == "rclick":
            pg.click(button='right')
            continue
        
        elif key.split(" ")[0] == "REM":
            continue

        elif key.split(" ")[0] == "DELAY":
            time.sleep(float(key.split(" ")[1])/1000)
            continue
        
        elif key == "GUI":
            pg.press('win')
            continue

        elif key.split(" ")[0] == "GUI":
            pg.hotkey("win",key.split(" ")[1])
            continue

        elif key.split(" ")[0] == "STRING":
            pg.write(key.split(" ")[1],0.01)
            continue
        
        elif key.split(" ")[0].upper() == key.split(" ")[0] and len(key.split(" ")) == 2:
            pg.hotkey(key.split(" ")[0].lower(), key.split(" ")[1].lower())
            continue

        elif key.lower() in valid:
            pg.press(key.lower())
            
        else:
            if str(key) in valid:
                pg.press(key)
                time.sleep(0.01)
                continue
            else:
                pg.write(key,0.01)
                continue

if __name__ == "__main__":
    args = sys.argv # Aquí iría el argparse
    if len(args)-1 > 0: # Aquí si hay un nombre de archivo
        kfn = args[1] # Keys filename
        if len(args)-1 > 1:
            if args[2] == "q":
                quiet = True
        main(keysfilename=kfn)
    else:
        setup()