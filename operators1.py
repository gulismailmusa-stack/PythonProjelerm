# 1-Atama operatorleri

# x=10
# y=20
# z=30

# x,y,*z=10,20,30,40

# print(x,y,z)

# x += 5  # x = x + 5
# x -= 5  # x = x - 5
# x /= 5  # x = x / 5
# x *= 5  # x = * + 5
# x %= 5  # x = x % 5
# x //= 5 # x = x // 5
# x **= 5 # x = x **5
# 2-Karşılastirma operatorleri
x ,y ,z = 5 ,20 ,20
sonuc=(x == y) # False
sonuc=(y == z) # True
sonuc=(y != z) # False

email = "info@sadıkturan.com"
password = "12345"
isEmail = (email == "info@sadıkturan.com") #True
isPassword = (password == "123458") #True

sonuc = (x <= y)
sonuc = (x > y)
print(sonuc)
# 3-Mantıksal operatorler


#c- Not
#sonuc= isEmail and isPassword
#sonuc = 5 < x < 15
durum1 = x > 5
durum2 = x < 15 
#sonuc = durum1 and durum2
#b- Or 
# ehliyer için en az lise mezunu ve en az yas 18 olmalı
mezuniyet = "ilkokul"
yas = 18 
sonuc =(mezuniyet == "lise" or mezuniyet == "lisans" or mezuniyet == "onlisans") and (yas >= 18)

#c- Not
sonuc=not(True)
sonuc=not(False)
print(sonuc)

#identity operarors
a=[1,2,3]
b=a
print(b is not a)
meyveler=["muz","elma"]
print("muz" not in meyveler)
