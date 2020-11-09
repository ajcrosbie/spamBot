import pyautogui
import time


def beeM():
    time.sleep(5)
    f = open('BeeMovie.txt', 'r')
    i = 0
    for r in f:
        i = i+1
        pyautogui.typewrite(r)
        pyautogui.press('enter')
        time.sleep(0.8)
        print(i)

    f.close()


def ping():
    who = input('who to ping?')
    num = int(input('how many times?'))
    message = input('message?')
    time.sleep(5)
    for i in range(num):
        if who == 'everyone':
            if message == 'n':
                pyautogui.typewrite('@')
                pyautogui.typewrite(who)
                pyautogui.press('enter')
            else:
                pyautogui.typewrite('@')
                pyautogui.typewrite(who)
                pyautogui.typewrite(' ')
                pyautogui.typewrite(message)
                pyautogui.press('enter')

        else:
            if message == 'n':
                pyautogui.typewrite('@')
                pyautogui.typewrite(who)
                pyautogui.press('enter')
                pyautogui.press('enter')
            else:
                pyautogui.typewrite('@')
                pyautogui.typewrite(who)
                pyautogui.press('enter')
                pyautogui.typewrite(' ')
                pyautogui.typewrite(message)
                pyautogui.press('enter')

        time.sleep(0.6)
        if i == num//2:
            print(i)


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


if __name__ == "__main__":
    main()
