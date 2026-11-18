import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window=tb.Window(theme="darkly")

window.title("TTK BOOTSTRAP")
window.geometry("700x500")

def scaler(e):
    lbl.config(text=int(s1.get()))
    if(s1.get()<50):
        lbl.config(bootstyle="success inverse")
    else:
        lbl.config(bootstyle="danger inverse")
s1=tb.Scale(window,bootstyle="primary",orient="horizontal",command=scaler,from_=0,to=100)
s1.pack(pady=20,pady=20,fill=X)

s2=tb.Scale(window,bootstyle="primary",orient="verical")
s2.pack(pady=20,pady=20,fill=Y)

lbl=tb.Label(window,text="",bootstyle="danger toggle invere",font=("Arial",25))
lbl.pack(padx=20,pady=10)
window.mainloop()
