from tkinter import *
root=Tk()
root.geometry('700x233')
# root.maxsize(700,500)
# root.minsize(700,200)
root.title('PyCharm Editor')
# attributes of lable() and pack() function

'''
==========================
 IMPORTANT LABLE OPTIONS
==========================
1.text - adds the text 
2.bd & background - adds background
3.fg - foreground
4.fonts - sets the font 
        A. font=("comicsansns", 9, "bold")
        B. font="comicsansns" 9 "bold"
5.padx - padding on x
6.pady - padding on y
7.relief - border styling -- SUNKEN, REAISED, GROOVE, RIDGE
8.borderwidth - sets the width of the border 

==========================
  IMPORTANT PACK OPTION
==========================
1. anchor - nw,ne,sw,se
2. side - top, botton, left, right (BY DEFAULT THE SIDE IS TOP)
3. fill - X,Y
4. padx - 
5. pady -

NOTE:-fill=Y works only for side=left,right
'''


l=Label(text='''Globalization, or globalisation, \nIt is the process of interaction and integration among people, \ncompanies, and governments worldwide. Globalization has accelerated since the 18th century due to advances \nin transportation and communication technology.''',bg="black",fg="white",padx=23,pady=20,font=("comicsansns", 9, "bold"),borderwidth=10,relief=RIDGE)
# l.pack(side=BOTTOM,fill=X)
l.pack(side=LEFT,fill=Y,padx=20,pady=50)





root.mainloop()
