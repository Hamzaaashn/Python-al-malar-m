sayılar = []

for sayı in range(1,101):
    sayı / range(2,sayı)
    for sayı1 in range(2,sayı):
            if sayı % sayı1 == 0 :
                 sayılar.append(sayı)

print(sayılar)