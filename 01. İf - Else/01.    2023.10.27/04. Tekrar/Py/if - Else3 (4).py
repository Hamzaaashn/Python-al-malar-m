limit = 20
girilen_kg  = float(input("Lütfen Yükünüzün Ağırlığını Girin :\n"))
ek_ücret = 10

if girilen_kg <= limit :
    print("Ücret Ödemenize Gerek Yok")

else :
    print("Ödemeniz Gereken Ücret",ek_ücret * (girilen_kg - 20))