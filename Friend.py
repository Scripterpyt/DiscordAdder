import os
from colorama import Fore
import time
import sys
import requests
import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import requests
import sys

Tk().withdraw()
root = tkinter.Tk()
root.withdraw()


def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.05)


def RPT():
    while 1:
        Friendz()
        os.system("pause")


def Friendz():
    global raw
    os.system("cls && title Friendz")
    design = """
\u001b[38;5;46m                                                  ____ \u001b[38;5;47m ____  \u001b[38;5;48m __ \u001b[38;5;49m ____ \u001b[38;5;50m __ _  \u001b[38;5;51m ____  
\u001b[38;5;46m                                                 (  __)\u001b[38;5;47m(  _ \ \u001b[38;5;48m(  )\u001b[38;5;49m(  __)\u001b[38;5;50m(  ( \ \u001b[38;5;51m(    \ 
\u001b[38;5;46m                                                  ) _) \u001b[38;5;47m )   / \u001b[38;5;48m )( \u001b[38;5;49m ) _) \u001b[38;5;50m/    / \u001b[38;5;51m ) D ( 
\u001b[38;5;46m                                                 (__)  \u001b[38;5;47m(__\_) \u001b[38;5;48m(__)\u001b[38;5;49m(____)\u001b[38;5;50m\_)__) \u001b[38;5;51m(____/ 

\u001b[38;5;46m                                                         Made by albaner#0599
                                    

    """
    print(design)
    time.sleep(3)
    token_filename = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")), title="Choose Your TokensList!")
    try:
        with open(token_filename, 'r') as UseFile:
            print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}Combo{Fore.RED}List:{Fore.LIGHTWHITE_EX}] ' + Fore.LIGHTGREEN_EX + token_filename)
            tokensline = sum(1 for _ in UseFile)
    except:
        print(f'{Fore.RED} [{Fore.LIGHTGREEN_EX}-{Fore.RED}] Not existing combo File')
        time.sleep(1)

    print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}Token{Fore.RED}List:{Fore.LIGHTWHITE_EX}] ' + Fore.LIGHTGREEN_EX + str(tokensline))

    print("")
    idofuser = input(Fore.RED + "Please enter the id of the target: ")
    print("")
    print("")

    with open(token_filename, 'r') as f:
        tokens = f.readlines()
        for x in tokens:
            token = x.rstrip()
            headers = {
                'Authorization': token
            }
            messagesend = requests.put(f"https://discord.com/api/v8/users/@me/relationships/{idofuser}",json={}, headers=headers)
            if messagesend.status_code == 204:
                print(f'{Fore.RED}[{Fore.LIGHTWHITE_EX}+{Fore.RED}]{Fore.GREEN} Friend Request sent ;)')
            else:
                print(f'{Fore.RED}[{Fore.LIGHTWHITE_EX}-{Fore.RED}]{Fore.RED} Something went wrong..')


RPT()