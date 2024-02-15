ürün1 = float(input("Lütfen İlk Ürünün Fiyatını Girin :\n"))
ürün2 = float(input("İkinci Ürünün Fiyatını Girin :\n"))

tutar = ürün1 + ürün2
indirim_miktarı = 0.25


if tutar <= 200 :
    print("Ödemeniz Gereken Fiyat :\n",tutar)

else :
    tutar -= tutar * indirim_miktarı
    print("Ödemeniz Gereken İndirimli Fiyat :\n",tutar)