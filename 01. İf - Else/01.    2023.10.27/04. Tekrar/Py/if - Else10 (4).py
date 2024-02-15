süre = float(input("Lütfen Otoparkta Kaldığınız Süreyi Girin :\n"))

if süre <= 1 :
    print("Ödemeniz Gereken Ücret :\n","5 TL")

elif süre <= 5 :
    print("Ödemeniz Gereken Ücret :\n",süre * 4,"TL")

else:
    print("Ödemeniz Gereken Ücret :\n",süre * 3,"TL")