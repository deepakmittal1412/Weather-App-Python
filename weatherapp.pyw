from weather import Weather
from tkinter import *


def res():
    try:
        weather = Weather()
        location = weather.lookup_by_location(ent.get())
        condition = location.condition()
        st = condition.text()
        temp = condition.temp()
    except:
        win = Tk()
        win.minsize(250, 150)
        win.resizable(0, 0)
        win.propagate()
        win.title("Weather")
        win.config(bg='light sky blue')
        Label(win, text="Invalid Location", font=('Helvetica', 15, 'bold italic'), bg="light sky blue").pack(expand=YES)
    else:
        win = Tk()
        win.minsize(250, 150)
        win.resizable(0, 0)
        win.propagate()
        win.title("Weather")
        win.config(bg='light sky blue')
        Label(win, text=st, font=('Helvetica', 15, 'bold italic'), bg="light sky blue").pack(expand=YES)
        Label(win, text=temp + ' degrees', font=('Helvetica', 15, 'bold italic'), bg="light sky blue").pack(expand=YES)


root = Tk()
root.minsize(250, 150)
root.resizable(0, 0)
root.propagate()
root.title("Weather")
root.config(bg='light sky blue')

Label(root, text="WEATHER REPORT", font=('Helvetica', 15, 'bold italic'), bg="light sky blue").pack(side=TOP)
Label(root, text="Location : ", font=('Helvetica', 15), bg="light sky blue").pack(side=LEFT)
ent = Entry(root)
ent.insert(0, '')
ent.pack(side=LEFT)
b1 = Button(root, text="Submit", bg='peach puff', command=res).pack(side=BOTTOM)
root.mainloop()
