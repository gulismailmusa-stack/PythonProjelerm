class Ogrenci(): #python yapayzekaylatekrargünü7.py
    def __init__(self,ad,yas,not_bilgisi):
        self.ad=ad
        self.yas=yas
        self.not_bilgisi=not_bilgisi
    def __str__(self):
       return f"{self.ad},{self.yas},{self.not_bilgisi}"
ogrenci1=Ogrenci("salih",15,90)
ogrenci2=Ogrenci("kerem",22,30)
print(f"Ad : {ogrenci1.ad} , Yas : {ogrenci1.yas} , Not : {ogrenci1.not_bilgisi}")
print(f"Ad : {ogrenci2.ad} , Yas : {ogrenci2.yas} , Not : {ogrenci2.not_bilgisi}")
print(ogrenci1)
print(ogrenci2)
        