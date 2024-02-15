sayılar = [1,7,10,34,2,8]
en_büyük = 0

while True :
    en_büyük = 0

    for sayı in sayılar :
        if sayı > en_büyük:
            en_büyük = sayı

    print("En Büyük Sayı :\n",en_büyük)
    break