def işlemci(x):
    
    if  x == "i7" or x == "i9" or x == "İ7" or x == "İ9":
        return x
    

def ram(ram_boyutu):

    if ram_boyutu == "8 GB" or  ram_boyutu == "16 GB" or  ram_boyutu == "32 GB" or  ram_boyutu == "64 GB" or  ram_boyutu == "128 GB" or ram_boyutu =="8" or ram_boyutu == "16" or ram_boyutu == "32" or ram_boyutu == "64" or ram_boyutu == "128" :
        return ram_boyutu
    
girilen_işlemci = input("İşlemcinizi Girin :\n")
girilen_ram = input("Ram Boyutunu Girin :\n")

işlemciiiiii = işlemci(girilen_işlemci)
rammm = ram(girilen_ram)


if işlemciiiiii and rammm :
    print("Kuruluma Uygun")

else :
    print("Kuruluma Uygun Değil")