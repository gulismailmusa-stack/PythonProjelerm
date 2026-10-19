def toplama (x,y):
    return x+y
def cikarma (x,y):
    return x-y
def carpma (x,y):
    return x*y
def bolme (x,y):
    return x/y

while True:
    print("işlem seciniz.")
    print("toplama işlemi için 1'e basiniz.")
    print("cikarma işlemi için 2'e basiniz.")
    print("carpma işlemi için 3'e basiniz.")
    print("bolme işlemi için 4'e basiniz.")

    işlem=input("seciminizi giriniz: ")

    sayi1=int(input("birinci sayiyi giriniz: "))
    sayi2=int(input("ikinci sayiyi giriniz: "))

    if(işlem=="1"):
        print("işlem sonucu: ",toplama(sayi1,sayi2))
        
    elif(işlem=="2"):
        print("işlem sonucu: ",cikarma(sayi1,sayi2))
        
    elif(işlem=="3"):
        print("işlem sonucu: ",carpma(sayi1,sayi2))
        
    elif(işlem=="4"):
        print("işlem sonucu: ",bolme(sayi1,sayi2))
        
    else:
        print("hatali sayi girdiniz")
