"""
1-100 arasında rastgele üreticlecek bir sayıyı asagı yukarı ifadelerle buldurmaya calısın 
(hak =5)
**"random modulu" için python random seklinde arama yapın
100 uzerinden puanlama yapın her soru 20 puan 
hak bilgisini kullanıcıdan alın ve her spru belirtilen can sayısı uzerinden hesaplansın 

"""
import random
sayi = random.randint(1,100)

hak =5
while hak>0 :
    hak-=1
    tahmin=int(input('tahmin: '))

    if sayi == tahmin:
        print('tebrikler bildiniz')
        break

    elif sayi > tahmin:
        print('yukarı')

    else:
        print('asagı')

    if hak ==0:
        print(f" hakkınız bitti. tutulan sayi:{sayi}")



