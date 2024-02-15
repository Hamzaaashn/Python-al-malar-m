def ücret_alma(Ürün):
    ücret = float(input(Ürün +"Ürünün Fiyatını Girin :\n"))
    return ücret



alınan_ücret_1 = ücret_alma("1. ")
alınan_ücret_2 = ücret_alma("2. ")



def işlem(ücret1 , ücret2):
    toplam = ücret1 + ücret2

    if toplam <= 200:
        print("Ödenecek Ücret :\n",toplam)

    else :
        toplam -= toplam * 0.25
        print("Ödenecek İndirimli Tutar:\n",toplam)




işlem(alınan_ücret_1 , alınan_ücret_2)