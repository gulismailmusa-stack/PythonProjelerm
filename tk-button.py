# python tk-button.py
from tkinter import *
window=Tk()
window.geometry("500x500")
Button(window,text="tikla").pack()
Button(window,text="tikla",padx=10).pack()
Button(window,text="tikla",padx=30).pack()
Button(window,text="tikla",padx=30,pady=30,state="disabled").pack()

def btnclick():
    lblsonuc["text"]+=input.get() + " "
    input.delete(0,"end")

input=Entry(window)
lblsonuc=Label(window)
Button(window,text="goster",command=btnclick).pack()
Button(window,text="quit",command=window.quit).pack()
input.pack()
lblsonuc.pack()
window.mainloop()