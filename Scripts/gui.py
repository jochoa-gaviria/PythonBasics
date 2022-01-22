## Install libraries ##
# sudo apt-get install python3-tk 
## Install libraries ##

## Import libraries ##
from tkinter import *
## Import libraries ##


def kgToPoundsToOunces():
    try:
        kg = float(kgValue.get())
        g=kg*1000
        grams.delete("1.0", END)
        grams.insert(END, g)
        p=kg*2.20462
        pounds.delete("1.0", END)
        pounds.insert(END, p)
        o=kg*35.274
        ounces.delete("1.0", END)
        ounces.insert(END, o)
    except: print("please enter a number")

window = Tk()

kgLabel=Label(window, text="Kilograms")
kgLabel.grid(row=0, column=2)
kgValue = StringVar()
kgEntry=Entry(window, textvariable=kgValue)
kgEntry.grid(row=1, column=2)

b1 = Button(window, text="Calculate", command=kgToPoundsToOunces)
b1.grid(row=1, column=3)


kgLabel=Label(window, text="Grams")
kgLabel.grid(row=2, column=1)
grams=Text(window, height=1, width=20)
grams.grid(row=3, column=1)

kgLabel=Label(window, text="Pounds")
kgLabel.grid(row=2, column=2)
pounds=Text(window, height=1, width=20)
pounds.grid(row=3, column=2)

kgLabel=Label(window, text="Ounces")
kgLabel.grid(row=2, column=3)
ounces=Text(window, height=1, width=20)
ounces.grid(row=3, column=3)

window.mainloop()