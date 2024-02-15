import random

sayı = random.randint(0,20)

while True :

    girilen_sayı = int(input("Sayı Girin :\n"))

    if sayı == girilen_sayı :
        
        print("Doğru Tahmin")
        break

    elif girilen_sayı > sayı :

        print("Daha Küçük Bir Sayı Deneyin")


    elif girilen_sayı < sayı :

        print("Daha Büyük Bir Sayı Deneyin")
    