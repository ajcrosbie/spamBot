import pyautogui
import time
import tkinter as tk


class spammer():
    def __init__(self):
        self.root = tk.Tk()

    def ping(self):
        time.sleep(5)
        who = self.Who.get()
        message = self.mes.get()
        num = int(self.num.get())
        for i in range(num):
            if who == 'everyone':
                if message == '':
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
                if message == '':
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
            time.sleep(0.5)
        self.root.destroy()
        quit()

    def tragedy(self):
        num = int(self.num.get())
        for i in range(num):
            c = open('tragedy.txt', 'r')
            for v in c:
                pyautogui.typewrite(v)
                pyautogui.press('enter')
                time.sleep(0.6)

    def SpamMessage(self):
        message = self.message.get()
        num = int(self.num.get())
        time.sleep(3)
        for i in range(num):
            pyautogui.typewrite(message)
            pyautogui.press('enter')
            time.sleep(0.5)
        self.root.destroy()
        quit()

    def bee(self):
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

    def Mping(self):
        self.root.destroy()
        self.root = tk.Tk()

        Wlable = tk.Label(self.root, text='who to ping?')
        self.Who = tk.Entry(self.root)

        Mlable = tk.Label(self.root, text='message?')
        self.mes = tk.Entry(self.root)

        Nlable = tk.Label(self.root, text='how many times?')
        self.num = tk.Entry(self.root)

        EB = tk.Button(self.root, text='enter', command=self.ping)

        Wlable.grid(row=0)
        self.Who.grid(row=0, column=1)
        Mlable.grid(row=1)
        self.mes.grid(row=1, column=1)
        Nlable.grid(row=2)
        self.num.grid(row=2, column=1)
        EB.grid(row=3)

        self.root.mainloop()

    def Mtragedy(self):
        self.root.destroy()
        self.root = tk.Tk()

        nlable = tk.Label(self.root, text='how many times?')
        self.num = tk.Entry(self.root)
        EB = tk.Button(self.root, text='enter', command=self.tragedy)

        nlable.grid(row=0)
        self.num.grid(row=0, column=1)
        EB.grid(row=1)

        self.root.mainloop()

    def Mmessage(self):
        self.root.destroy()
        self.root = tk.Tk()

        Mlable = tk.Label(self.root, text='what is your message?')
        self.message = tk.Entry(self.root)

        Nlable = tk.Label(self.root, text='how many times')
        self.num = tk.Entry(self.root)

        EB = tk.Button(self.root, text='enter', command=self.SpamMessage)

        Mlable.grid(row=0)
        self.message.grid(row=0, column=1)

        Nlable.grid(row=1)
        self.num.grid(row=1, column=1)

        EB.grid(row=2)
        self.root.mainloop()

    def menu(self):
        PingB = tk.Button(self.root, text='ping', command=self.Mping)
        tragedyB = tk.Button(self.root, text='tragedy', command=self.Mtragedy)
        messageB = tk.Button(self.root, text='message', command=self.Mmessage)
        beeB = tk.Button(self.root, text='bee', command=self.bee)

        PingB.grid(row=0)
        tragedyB.grid(row=1)
        messageB.grid(row=0, column=1)
        beeB.grid(row=1, column=1)

        self.root.mainloop()


if __name__ == "__main__":
    spam = spammer()
    spam.menu()
