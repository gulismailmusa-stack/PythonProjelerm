kartsifresi= "1923"
bakiye=1000  
denemehakki=3              
print("x bankasina hos geldiniz")
kart_islem_durumu=True
islemdurumu= True
while islemdurumu:
    girilensifre=input("kart sifrenizi giriniz: ")
    if girilensifre!= kartsifresi:
        print("yanlis sifre,tekrar deneyiniz")
        denemehakki-=1
        print(denemehakki,"deneme hakkiniz kaldi")
        if denemehakki==0:
            print("kartiniz bloklandi.Banka ile gorusun")
            islemdurumu=False
       
    else:
        
        print("giris yapildi")
        print(""" 
        yapilacak islem seciniz
        ----------------------------
        1- para cekme
        2- para yatirma 
        3- bakiye sorgulama
        4- cıkıs
        """)
        while kart_islem_durumu:
         print("------------------------------")
         islemno=input("islem numarasini giriniz")
         if islemno=="4":
            print("cikis yapildi")
            islemdurumu=False
            kart_islem_durumu=False
         elif islemno=="3":
            print("Toplam bakiye:",bakiye,"₺")
         elif islemno=="2":
            yatiralicakmiktar=int(input("yatirilacak miktar:"))
            bakiye+= yatiralicakmiktar
            print("islem gerceklesti")
         elif islemno =="1":
            cekilecekMiktar=int(input("cekilecekMiktar:"))
            if cekilecekMiktar>bakiye:
               
             print("yetersiz bakiye bakiye")
            else:
               bakiye -=cekilecekMiktar
               print("islem gerceklestirildi")
         