#!/usr/bin/python3
import tkinter
import tkinter.messagebox


def reply():
    tkinter.messagebox.showinfo(title='popup', message='Button pressed!')


window = tkinter.Tk()
button = tkinter.Button(window, text='press', command=reply)
button.pack()
window.mainloop()
