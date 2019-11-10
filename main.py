import math
import shelve2
from tkinter import *
from decimal import *

db = shelve2.shelve("planets")
getcontext().prec = 6

def comma(number):
    return f'{float(number):,}'


def percent(per, whole):
    return (per * whole) / 100.0


class astro:
    def pri(self, event):
        w = event.widget
        x = int(w.curselection()[0])
        value = w.get(x)
        value = value.split('|')
        au = math.pow(float(value[1]), 1/3)**2
        a = Decimal(self.grav)
        b = Decimal(self.fracuau ** 2)
        print(f'{a}/{b}')
        self.desc.set(
            f"Name: {value[0]}\nYear Length: {comma(value[1])} Years\nDays: {comma(int(float(value[1]) * 365))}\nGrav From Star: {a/b}"
        )

    def dele(self):
        x = self.listbox.curselection()[0]
        self.desc.set('')
        slice = self.listbox.get(x).split(' | ')[0]
        self.listbox.delete(x, x)
        del db[slice]

    def __init__(self, per_sun):
        self.per_sun = per_sun
        self.grav = percent(per_sun, 274)
        db['per_sun'] = per_sun
        self.radius = percent(per_sun, 695700)
        self.fracuau = percent(per_sun, 216)
        self.mass = percent(per_sun, 100) * (100 ** 9)
        self.au = 150
        self.desc = StringVar()
        self.des = Label(root, textvariable=self.desc, justify=LEFT)
        self.des.grid(column=0, row=4)
        self.instr1 = Label(root, text="Distance in AU")
        self.instr2 = Label(root, text="Planet Name")
        self.instr1.grid(column=0, row=0)
        self.instr2.grid(column=0, row=1)
        self.distance = Entry(root, textvariable=dist)
        self.name = Entry(root, textvariable=name)
        self.distance.grid(column=1, row=0)
        self.name.grid(column=1, row=1)
        self.enter = Button(root, text='New Planet', command=self.get_planet_orbit_time)
        self.enter.grid(column=0, row=5)
        # ListBox Stuff
        self.listbox = Listbox(root)
        self.listbox.bind('<<ListboxSelect>>', self.pri)
        self.delete = Button(root, text='Delete', command=self.dele)
        self.delete.grid(column=2, row=5)
        self.listbox.grid(column=1, row=4)
        self.scroll = Scrollbar(root)
        self.scroll.grid(column=2, row=4)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listbox.yview)
        for k, v in eval(str(db)).items():
            if k != "per_sun":
                self.listbox.insert(END, f'{k} | {v}')
        root.mainloop()

    def get_planet_orbit_time(self):
        try:
            distance = float(self.distance.get()) * self.au
            planet_distance = distance / self.au
            db[self.name.get()] = str(round(math.sqrt(planet_distance ** 3) / (self.per_sun / 100), 3))
            self.listbox.insert(END, f'{self.name.get()} | ' + str(
                round(math.sqrt(planet_distance ** 3) / (self.per_sun / 100), 3)))
        except ValueError:
            pass
        name.set('')
        dist.set('')


def create():
    a.pack_forget()
    b.pack_forget()
    c.pack_forget()
    astro(int(c.get()))


root = Tk()
root.title("AstroVerse")
name = StringVar()
dist = StringVar()

if db['per_sun'] is not None:
    astro(db['per_sun'])
else:
    a = Label(root, text="x % of sun")
    a.pack(side=LEFT)
    c = Entry(root)
    c.pack(side=LEFT)
    b = Button(root, text="Enter", command=create)
    b.pack(side=LEFT)
    root.mainloop()
