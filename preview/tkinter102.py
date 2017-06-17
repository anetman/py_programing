#!/usr/bin/python3
import tkinter
import tkinter.messagebox


class MyGui(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self, parent)
        button = tkinter.Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        tkinter.messagebox.showinfo(title='popup', message='Button pressed!')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
