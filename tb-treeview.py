import ttkbootstrap as tb 
from tkinter import *

window=tb.Window(theme="darkly")

window.title("TTK BOOTSTRAP")
window.geometry("850x700")

my_frame=tb.Frame(window,bootstyle="light",padding=20)
my_frame.pack()

s1=tb.Scrollbar(my_frame,orient=VERTICAL)
s1.pack(side=RIGHT,fill=Y)
twn=tb.Treeview(window,show="headings",bootstyle="primary",height=20,yscrollcommand=s1.set)
twn.pack()

s1.config(command=twn.yview)
#column
twn["column"]=("id","firstname","lastname","email")
twn.column("#0",width=50,minwidth=30,anchor="w")
twn.column("#1",width=200,minwidth=100,anchor="w")
twn.column("#2",width=200,minwidth=100,anchor="w")
twn.column("#3",width=200,minwidth=100,anchor="w")

#headings
twn.heading("id",text="id")
twn.heading("firstname",text="Ad")
twn.heading("lastname",text="SoyAd")
twn.heading("email",text="Email")

#EXAMPLEDATA
ogrenciler=[""]
for n in range(0,100):
    ogrenciler.append({F"{n}",f"ad{n}",f"soyad{n}",f"emain{n}"})
for ogrenci in ogrenciler:
    twn.insert("",END,values=(ogrenci[0],ogrenci[1],ogrenci[2],ogrenci[3]))
twn.insert("",END,values=("ahmet","yilmaz","ali.gmail.com"))
twn.insert("",END,values=("ALİ","yilmaz","ali.gmail.com"))
twn.insert("",END,values=("hASAN","yilmaz","ali.gmail.com"))

window.mainloop()