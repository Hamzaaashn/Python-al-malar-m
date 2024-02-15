def bir_saat(x):
    if x == 1 :
        print("Ödemeniz Gereken Ücret 5 TL")


def bir_beş_arası(x):
    if x > 1 and x <= 5 :
        print("Ödemeniz Gereken Ücret",x * 4,"TL")

def beş_saat_fazlası(x):
    if x > 5 :
        print("Ödemeniz Gereken Ücret",x * 3,"TL")

süre = int(input("Otoparkta Kaldığınız Süreyi Girin :\n"))

bir_saat(süre)
bir_beş_arası(süre)
beş_saat_fazlası(süre)