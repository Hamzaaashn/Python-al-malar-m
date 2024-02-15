kaldığın_süre = float(input("Otoparkta Kaldığınız Süreyi Girin :\n"))

if  kaldığın_süre == 0  or kaldığın_süre == 1 :
    print("Ödemeniz Gereken Tutar :\n ","5 TL") 

elif kaldığın_süre <= 5 :
    print("Ödemeniz Gereken Tutar :\n", kaldığın_süre * 4)
else:
    print("Ödemeniz Gereken Tutar :\n", kaldığın_süre * 3)