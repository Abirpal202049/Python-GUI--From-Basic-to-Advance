# Creating our first GUI

# LABLE IS A WIZID in tkinter in the user do not interact

from tkinter import *

root=Tk()
# width x height
root.geometry('500x500') # It defines the geometry of the GUI window
# width, height
root.minsize(300,300) # It defines the minimum size of the GUI window
# width, height
root.maxsize(700,700) # It defines the minimum size of the GUI window

a=Label(text='Hellow everybody, Welcome to my GUI')
b=Label(text='This is my first GUI')
a.pack()
b.pack()

root.mainloop()