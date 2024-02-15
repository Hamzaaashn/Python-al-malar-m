limit = 20
ek_ücret = 10

yolcu_valiz_hacmi = float(input("Yük Ağırlığını Giriniz :\n"))

if yolcu_valiz_hacmi > 20 :
    print("Ödemeniz Gereken Tutar :\n",(yolcu_valiz_hacmi - limit)*ek_ücret)
else:
    print("Ödemeniz Gereken Bir Ücret Yok")

