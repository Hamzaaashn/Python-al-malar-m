def değeral(x):
    değer = float(input(x + " Girin :\n"))
    return değer

boy = değeral("Boyunuzu")
ağırlık = değeral("Ağırlığınız")
vki = ağırlık / (boy * boy)



def zayıf():
    if vki <= 18 :
        return True

    
def normal():
    if vki <= 25 :
        return True

    
def kilolu():
    if vki <= 30 :
        return True

    
def obez():
    if vki <= 35 :
        return True

    
def ciddi_obez():
    if vki > 35 :
        return True

    


if zayıf() == True :
    print("Zayıf")

elif normal() == True :
    print("Normal")

elif kilolu() == True :
    print("Kilolu")

elif obez()  == True :
    print("Obez")

elif ciddi_obez() == True :
    print("Ciddi Obez")