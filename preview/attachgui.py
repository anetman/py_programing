#!/usr/bin/python3
import tkinter
from tkinter102 import MyGui

'''main app window'''
mainwin = tkinter.Tk()
tkinter.Label(mainwin, text=__name__).pack()

'''popup window'''
popup = tkinter.Toplevel()
tkinter.Label(popup, text='Attack').pack(side=tkinter.LEFT)
MyGui(popup).pack(side=tkinter.RIGHT)
mainwin.mainloop()
