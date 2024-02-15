while True :

    sayı = int(input("1 ile 5 Arasında Bir Sayı Giriniz :\n"))

    if sayı < 1 or sayı > 5 :
        print("! 1 İle 5 Arasında !")
        print()

    elif sayı == 3 :

        print("3 Sayısı Girildi Ve Döngü Sona Erdi")
        break