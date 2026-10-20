# python tk-uygulama-toplama.py
from tkinter import *
window=Tk()
window.geometry("300x250")
window.resizable(height=False,width=False)
window.columnconfigure(0,weight=1)
window.columnconfigure(0,weight=3)
def toplama (x,y):
    return x+y
sayi1=Label(window,text="sayi1")
sayi1.grid(sticky="w",column=0,row=0,padx=4,pady=4,command=toplama)
sayi1_entry=Entry(window,command=toplama)
sayi1_entry.grid(sticky="we",column=1,row=0,padx=5,pady=5)
sayi2=Label(window,text="sayi2")
sayi2.grid(column=0,row=1,sticky="we",padx=5,pady=5)
sayi2_entry=Entry(window,command=toplama)
sayi2_entry.grid(column=1,row=1,sticky="we",padx=5,pady=5)
topla=Button(window,text="topla",command=toplama)
window.mainloop()