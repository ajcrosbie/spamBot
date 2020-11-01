import pyautogui
import time
time.sleep(5)


def beeM():
    f = open('BeeMovie.txt', 'r')
    for r in f:
        pyautogui.typewrite(r)
        pyautogui.press('enter')
        time.sleep(1)
    f.close()


def ping():
    who = input('who to ping?')
    num = int(input('how many times?'))
    for i in range(num):
        pyautogui.typewrite('@', who)
        pyautogui.press('enter')


def tragedy():
    num = int(input('how many tragedies?'))
    f = open('b')
    for i range(num):
