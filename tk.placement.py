# python tk.placement.py
from tkinter import *
window=Tk()
window.geometry("500x500")

lbl1=Label(window,text="Label 1")
lbl2=Label(window,text="Label 2")
lbl3=Label(window,text="Label 3")

# konumlandirma=>grid,place,pack
#pack
# lbl1.pack()
# lbl2.pack(side="right")
# lbl3.pack(side="bottom")
# grid 
# lbl1.grid(column=0,row=0)
# lbl2.grid(row=1,column=0)
# lbl3.grid(row=2,column=0)

# place
lbl1.place(x=20,y=20)
lbl2.place(x=100,y=20)
lbl3.place(x=180,y=20)
window.mainloop()