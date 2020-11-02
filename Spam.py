import pyautogui
import time


def beeM():
    time.sleep(5)
    f = open('BeeMovie.txt', 'r')
    for r in f:
        pyautogui.typewrite(r)
        pyautogui.press('enter')
        time.sleep(0.6)
    f.close()


def ping():
    who = input('who to ping?')
    num = int(input('how many times?'))
    time.sleep(5)
    for i in range(num):
        pyautogui.typewrite('@')
        pyautogui.typewrite(who)
        pyautogui.press('enter')
        time.sleep(0.6)


def tragedy():
    f = open('tragedy.txt', 'r')
    for c in f:
        pyautogui.typewrite(c)
        pyautogui.press('enter')
        time.sleep(0.6)
    f.close()


def main():
    type = input('what? bee, ping, darth ')
    if type == 'bee':
        beeM()
    elif type == 'ping':
        ping()
    elif type == 'darth':
        num = int(input('how many tragedies?'))
        time.sleep(5)
        for i in range(num):
            tragedy()


main()
