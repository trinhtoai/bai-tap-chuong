from tkinter import *

a=Tk()
a.title('Welcome')
Checkbutton(a,text='First').grid(row=0,column=0)
Checkbutton(a,text='Second').grid(row=0,column=2)
Checkbutton(a,text='Third').grid(row=0,column=3)
Button(a,text="Click me").grid(row=0,column=4)

a.mainloop()
