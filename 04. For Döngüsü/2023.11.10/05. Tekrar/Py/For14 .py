import random

sayı = random.randint(0,20)
while True :

    girilen_sayı = int(input("0 İle 20 Arasında Bir Sayı Girin :\n"))

    if sayı == girilen_sayı :
        print("Doğru Tahmin")
        break

    elif girilen_sayı > sayı :
        print("Daha Küçük Bir Sayı Deneyiniz")

    elif girilen_sayı < sayı :
        print("Daha Büyük Bir Sayı Deneyiniz")