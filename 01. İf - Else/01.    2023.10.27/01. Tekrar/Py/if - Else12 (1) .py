print("Vücut Kitle İndeksinizi Bulmamız İçin Boyunuzu Ve Kilonuzu Sisteme Giriniz\n")

boy = float(input("Lütfen Boyunuzu Metre Cinsinden örn(x.xx)  Yazın\n"))
ağırlık = float(input("Lütfen Ağırlığınızı Girin\n"))

vki = ağırlık/(boy*boy)

if (vki >=18 and vki < 25) :
    print("Vücut Kitle İndeksiniz :\n","Normal")
elif(vki >=25 and vki < 30):
    print("Vücut Kitle İndeksiniz :\n","Kilolu")
elif(vki >=30 and vki < 35):
    print("Vücut Kitle İndeksiniz :\n","Obez")
elif(vki >=35):
    print("Vücut Kitle İndeksiniz :\n","Ciddi Obez")
