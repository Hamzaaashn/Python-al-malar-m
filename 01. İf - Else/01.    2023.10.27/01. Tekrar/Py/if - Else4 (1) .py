ürün1 = float(input("Birinci Ürünün Fiyatını Girin :\n"))
ürün2 = float(input("İkinci Ürünün Fiyatını Girin :\n"))
toplam = ürün1 + ürün2 
if toplam <= 200 :
    print("Ödemeniz Gereken Fiyat :\n",toplam)
else:
    indirim_tutarı = toplam * 0.25
    indirimli_fiyat = toplam - indirim_tutarı
    print("Ödemeniz Gereken İndirimli Fiyat :\n",indirimli_fiyat) 