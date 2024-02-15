bagaj_hakkı = 20
ek_ücret = 10



def bagaj():
    x = int(input("Bagaj Ağırlığını Girin :\n"))
 
    toplam = (x - bagaj_hakkı) * ek_ücret
    return x,toplam



def işlem(x,toplam):
    if x > bagaj_hakkı:
        print("Ödemeniz Gereken Ücret :\n", toplam)

    else :
        print("Ödemeniz Gereken Bir Ücret Yok")



girilen_bagaj_ağırlığı,ücret = bagaj()
işlem(girilen_bagaj_ağırlığı,ücret)