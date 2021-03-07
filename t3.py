from tkinter import *
# tkinter doesnot support .jpg format photos it only suppot .png format photos
from PIL  import Image, ImageTk  # pip install Pillow

'''
As tkinter doesnot support jpg format so we import PIL MODULE
PIL stands for Python Image Liabery it cointain a collection of Images
'''

root=Tk() # Building a basic GUI
root.geometry('1200x650')
root.minsize(1200,650)
root.maxsize(1200,650)

# photo= PhotoImage(file="2.png") # As it doesnot support jpg
'''
We are useing PhotoImage() only to use png format photos 
'''

image=Image.open('1.jpg') # image.open is used from PIL module to take the image
photo=ImageTk.PhotoImage(image) # here we are useing both the module tkinter and pil module
'''
We are useing the ImageTk with the PhotoImage() so to use jpg format photos
'''
text_lable=Label(text='J.A.R.V.I.S')# lable with text
text_lable.pack()

lable_photos=Label(image=photo)# lable with image
lable_photos.pack()

root.mainloop() # Event loop