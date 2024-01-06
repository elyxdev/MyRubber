import subprocess, os
from colorama import Fore, init
try:
    import pyinstaller
except:
    os.system("pip3 install pyinstaller")
import pyinstaller
init()

print(f"{Fore.RED}[{Fore.LIGHTRED_EX}+{Fore.RED}]{Fore.RESET} Espere mientras se compila su archivo...")
subprocess.call("pyinstaller --clean --onefile main.py --icon=./icon.ico", shell=True)