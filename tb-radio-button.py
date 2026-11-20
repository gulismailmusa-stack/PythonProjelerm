import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import * 

window=tb.Window(theme="darkly")

def get_value():
    lbl1.config(text=egitim_var.get())
window.title("TTK BOOTSTRAP")
window.geometry("700x500")
#liste=["Yuksek lisans","Lisans","OrtaOkul","IlkOkul"]
liste={"Yuksek Lisans":"1",
       "Lisans":"2",
       "Lise":"3",
       "OrtaOkul":"4",
       "IlkOkul":"5"
       }
egitim_var=StringVar()
for (text,value) in liste.items():
    tb.Radiobutton(window,bootstyle="primary toolbutton",value=value,text=text,variable=egitim_var,command=get_value).pack(pady=10)


#rb1=tb.Radiobutton(window,bootstyle="primary",value="lisans",text="lisaas",variable=egitim_var)
#rb1.pack(pady=20)

#rb2=tb.Radiobutton(window,bootstyle="primary",value="lise",text="lise",variable=egitim_var)
#rb2.pack(pady=20)

lbl1=tb.Label(window,bootstyle="warning")
lbl1.pack(pady=10)

btn=tb.Button(window,text="get value",bootstyle="primary",command=get_value)
btn.pack(pady=10)
window.mainloop()