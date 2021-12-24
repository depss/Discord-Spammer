#This is a spammer that sends a certain message a certain amount of times
#This can be used for discord but it is not limited to it
#WARNING!!! this spammer is not self aware, meaning that its going to run no matter what once the 5 seconds are up
#I am not responisble for what you do with this program
import ctypes
import os
import time
from colorama.ansi import Fore
import pyautogui
from colorama import init, Fore

init()
ctypes.windll.kernel32.SetConsoleTitleW('Discord Spammer By depss')

limit = 100
limit2 = 50

def banner():
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Discord Message Spammer')
    print('Written by: depss')
banner()

def spam_msg():
    banner()
    print('------------------------------------')
    print(Fore.YELLOW + 'Spamming in 5')
    time.sleep(1)
    os.system('cls')
    banner()
    print('------------------------------------')
    print(Fore.YELLOW + 'Spamming in 4')
    time.sleep(1)
    os.system('cls')
    banner()
    print('------------------------------------')
    print(Fore.YELLOW + 'Spamming in 3')
    time.sleep(1)
    os.system('cls')
    banner()
    print('------------------------------------')
    print(Fore.YELLOW + 'Spamming in 2')
    time.sleep(1)
    os.system('cls')
    banner()
    print('------------------------------------')
    print(Fore.YELLOW + 'Spamming in 1')
    time.sleep(1)
    os.system('cls')


def spam():
    print('------------------------------------')
    msg = input(Fore.LIGHTRED_EX + "What message would you like to spam: ")
    if len(msg) > limit:
        os.system('cls')
        print(Fore.RED + 'Error message must be 100 characters or shorter')
        print()
        print('Exiting in 5 Seconds')
        time.sleep(5)
        exit()
    else:
        pass
    print()
    try:
        amount = int(input(Fore.LIGHTMAGENTA_EX + "How many times would you like to spam the message: "))
    except ValueError:
        os.system('cls')
        print(Fore.RED + 'Error must be a number')
        print()
        print('Exiting in 5 Seconds')
        time.sleep(5)
        exit()
    if amount > limit2:
        os.system('cls')
        print(Fore.RED + 'Error Amount of times to send must be 50 or under')
        print()
        print('Exiting in 5 Seconds')
        time.sleep(5)
        exit()
    else:
        pass

    spam_msg()

    for x in range(amount):
        print(Fore.GREEN + 'SPAMMING')
        pyautogui.typewrite(msg)
        pyautogui.press('ENTER')
    os.system('cls')
    print(Fore.GREEN + 'Spam Succesfully Sent!')
    os.system('pause')
spam()
