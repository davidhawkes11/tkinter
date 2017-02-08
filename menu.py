import tkinter


def NewFile():
    print ("New File!")
def OpenFile():
    name = tkinter.askopenfilename()
    print (name)
def About():
    print ("This is a simple example of a menu")

    
root = tkinter.Tk()
menu = tkinter.Menu(root)
root.config(menu=menu)

filemenu = tkinter.Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

'''
Help Menu
'''
helpmenu = tkinter.Menu(menu)

menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

tkinter.mainloop()
