def soğuk(x):
    if x <= 5 :
        print("Hava Soğuk")


def ılık(x):
    if x >= 6 and x <= 14 :
        print("Hava Ilık")


def sıcak(x):
    if x >= 15 :
        print("Hava Sıcak")


hava = int(input("Hava Sıcaklığını Girin :\n"))

soğuk(hava)
ılık(hava)
sıcak(hava)