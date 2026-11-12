# python tk-entry.py 
from tkinter import *
window=Tk()
window.geometry("500x500")
input=Entry(window,
            width=50,
            font=("Arial 16"),
            )
lbl1=Label(window)
lbl1.pack()
inputValue=StringVar()
input["textvariable"]=inputValue
inputValue.set("deneme")
#METHODS
input.insert(0,"deneme")
input.delete(0,"end")
print(input.get())
lbl1["text"]=input.get()
print(inputValue.get())
input.pack()
window.mainloop()