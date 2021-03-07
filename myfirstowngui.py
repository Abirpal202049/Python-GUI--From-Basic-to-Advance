from tkinter import *

root=Tk()
root.title('   File    Edit    Selection   View    Go      Run     Terminal    Help')
root.geometry("800x700")
root.iconbitmap(r'boss.ico')


l=Label(text='Python 3.9.1 64-bit ',bg="gray",fg="white",font=("",11,""),padx='2',pady='2')
l.pack(side=BOTTOM,fill=X)
c=Label(text='EXPLORER                                              ...',bg='black',fg='white',padx=5,pady=5)
c.pack(side=LEFT,fill=Y,padx=60)

root.mainloop()

