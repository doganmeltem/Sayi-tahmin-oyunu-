import random
sayi = random.randint(1,100)

hak = int(input('kac hak kullanmak istersiniz:'))

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
        print(f"hakkınız bitti. tutulan sayi:{sayi}")

