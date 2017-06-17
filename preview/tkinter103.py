#!/usr/bin/python3
import tkinter
import tkinter.messagebox


def reply(name):
    tkinter.messagebox.showinfo(title='Reply', message='Hello %s!' % name)

top = tkinter.Tk()
top.title('Echo')
top.iconbitmap()

tkinter.Label(top, text="Enter your name:").pack(side=tkinter.TOP)
ent = tkinter.Entry(top)
ent.pack(side=tkinter.TOP)
btn = tkinter.Button(top, text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=tkinter.LEFT)

top.mainloop()
