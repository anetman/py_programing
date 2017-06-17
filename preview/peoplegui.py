#!/usr/bin/python3
import tkinter
import tkinter.messagebox
import shelve
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


def makeWidgets():
    global entries
    window = tkinter.Tk()
    window.title('People Shelve')
    form = tkinter.Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = tkinter.Label(form, text=label)
        ent = tkinter.Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    tkinter.Button(window, text="Fetch",
                   command=fetchRecord).pack(side=tkinter.LEFT)
    tkinter.Button(window, text="Update",
                   command=updateRecord).pack(side=tkinter.LEFT)
    tkinter.Button(window, text="Quit",
                   command=window.quit).pack(side=tkinter.RIGHT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        tkinter.messagebox.showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, tkinter.END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from person import Person
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()
