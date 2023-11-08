import os
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)
alfabe = ["a", "b", "c", "d", "e", "y", "z", "x"]
def calis():
    os.system("cls")
    print("Ad veya Nickname: ")
    girdi = input()
    for i in range(len(girdi)):
        kelime = girdi[:i+1]
        for harf in alfabe:
            if i == len(girdi) - 1:
                print(kelime + Fore.RED + (harf))
            else:
                print(kelime + Fore.RED + harf, end="\r")
            os.system("cls")
    os.system("cls")
    print(girdi)
    time.sleep(2)
calis()
