from tkinter import *

window=Tk()

frame1=Frame(window,width=300,height=23,bg="red")
frame1.pack(fill=X,side=LEFT)
frame2=Frame(window,width=400,height=123,bg="red")
frame2.pack(fill=X,side=LEFT)
frame3=Frame(window,width=500,height=223,bg="red")
frame3.pack(fill=Y,side=LEFT)
window.mainloop()