boy = float(input("Boyunuzu Metre Cinsinden örn(x.xx) Giriniz :\n"))
kilo = float(input("Ağırlığınızı Girin :\n"))

x = boy 
z = kilo 
vki = z / (x**2)

if vki <=18 :
    print("Zayıf")

elif vki <= 25 :
    print("Normal")

elif vki <= 30 :
    print("Kilolu")

elif vki < 35 :
    print("Obez")

else :
    print("Ciddi Obez")