#!/usr/bin/python3
import tkinter
import tkinter.messagebox
from tkinter102 import MyGui


class CustomGui(MyGui):
    def reply(self):
        tkinter.messagebox.showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    tkinter.mainloop()
