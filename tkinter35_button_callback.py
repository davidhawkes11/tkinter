"""
Python 3.5.x button callback
Source: http://effbot.org/tkinterbook/button.htm [with modifications]
"""
from tkinter import *

master = Tk()

def callback():
    print ("click! [if displayed, shows that the callback function was activated]")

b = Button(master, text="OK [click me!]", command=callback)
b.pack()

mainloop()
