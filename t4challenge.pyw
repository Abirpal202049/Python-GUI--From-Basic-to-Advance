def rtx():
    print('Abir Pal')



from tkinter import *
root= Tk()
root.title('Instant Health Check-up Kit')
root.geometry('400x700')
# root.iconbitmap('boss.ico')
root.iconbitmap('dy.ico')
root.maxsize(400,700)
root.minsize(400,400)

p=Label(text='Check Your Health Regularly...',bg='#00ff00',font=('Product Sans Light',20,'bold'),padx='10',pady='10',border=30,relief=RIDGE,borderwidth=5,activebackground='red',activeforeground='red')
p.pack(fill=X,padx='1',pady='1')

l=Button(root,text='Start Your Check-Up',bg='red',fg='#000000',font=('Monotype Corsiva', 25, 'bold'),borderwidth=5,relief=RAISED,padx='7',pady='7',height=30,activebackground='#00ff00',command=rtx)

l.pack(side=BOTTOM,pady='300')



root.mainloop()
# .pyw extension helps to remove the python console 