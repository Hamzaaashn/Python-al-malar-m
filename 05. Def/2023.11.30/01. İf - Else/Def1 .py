def notu (notu1):
    girilen_not = float(input(notu1 + " Notunuzu Girin :\n"))
    return girilen_not


def ortalama ():
    not1 = notu("1.")
    not2 = notu("2.")
    not3 = notu("Performans")

    Toplam = not1 + not2 + not3
    Ortalama= ( Toplam / 3)
    if Ortalama > 50 :
           print("Başarılı")
    elif Ortalama < 50 :   
           print("Başarısız")



ortalama()