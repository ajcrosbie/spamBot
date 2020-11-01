import pyautogui
import time


def beeM():
    time.sleep(5)
    f = open('BeeMovie.txt', 'r')
    for r in f:
        pyautogui.typewrite(r)
        pyautogui.press('enter')
        time.sleep(1)
    f.close()


def ping():
    time.sleep(5)
    who = input('who to ping?')
    num = int(input('how many times?'))
    for i in range(num):
        pyautogui.typewrite('@', who)
        pyautogui.press('enter')


def tragedy():
    f = open('tragedy.txt', 'r')
    for c in f:
        pyautogui.typewrite(c)
        pyautogui.press('enter')
        time.sleep(1)
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
