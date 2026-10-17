import random
sayi=random.randint(1,10)
can=int(input("kac hakta bilmek istersiniz: "))
hak=can
sayac=0
while hak==0:
  hak-=1
  sayac+=1
  tahmin=int(input("sayi tahmin ediniz: "))
  if(sayi == tahmin):
    print(f"tebrikler {sayac}. turda bildiniz. puan: {(100) - (100/can) * (sayac)}")
    break
  elif(sayi > tahmin):
    print("yukari")
  elif(sayi < tahmin):
    print("asagi")
  else:
    print(f"maalesef bilemediniz{sayi}")