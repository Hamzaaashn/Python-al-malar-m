import random

sayı = random.randint(1,20)

while True :
    
    girilen_sayı = int(input("Lütfen Bir Sayı Giriniz :\n"))

    if girilen_sayı == sayı :
        print("Doğru Tahmin :)")
        break

    elif girilen_sayı > sayı :
        print("\nDaha Küçük Bir Sayı Deneyiniz")

    elif girilen_sayı < sayı :
        print("\n Daha Büyük Bir Sayı Deneyiniz")