'''
to make a window of 733x434
'''
from tkinter import *
root=Tk()
root.geometry('733x434')
root.minsize(733,434)
root.maxsize(733,434)
lab=Label(text='''Welcome To PyCharm 
I welcome everybody to my PyCharm GUI
......''')
lab.pack()
root.mainloop()
