import random

sayı = random.randint(1,20)

while True :

    girilen_sayı = int(input("1 İle 20 Arasında Bir Sayı Giriniz :\n"))


    if girilen_sayı > 20 or girilen_sayı < 1 :

        print("!  1 İle 20 Arası  !")

    else:
        
        if sayı != girilen_sayı :

            if girilen_sayı < sayı :

                print("Daha Yüksek Bir Sayı Deneyiniz ")
                print()
                
            else:
                
                print("Daha Küçük Bir sayı Deneyiniz")
                print()
                
        else:
            
            print("Doğru Tahmin :)")
            break