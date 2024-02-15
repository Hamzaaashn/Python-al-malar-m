
sayı = int(input("Sayı girin :\n"))

def işlem(x):
    sonuç = 0
    for sayı in range(1,x):
        if sayı % 3 == 0 or sayı % 5 == 0 :
            sonuç += sayı
    print(sonuç)
            


işlem(sayı)
