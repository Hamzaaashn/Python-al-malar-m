print("İşlemcinizin Modelini Girin")
işlemci = input("i3\n"
                "i5\n"
                "i7\n"
                "i9\n")
print("Ram Boyutunu Seçin")

ram_boyutu = input("2 ""GB\n" 
                   "4 ""GB\n" 
                   "8 ""GB\n" 
                   "16 ""GB\n" 
                   "32 ""GB\n" 
                   "64 ""GB\n" 
                   "128 ""GB\n" )

if  (işlemci == "i7" or işlemci == "i9" or işlemci == "İ7" or işlemci == "İ9") and ( ram_boyutu == "8 GB" or  ram_boyutu == "16 GB" or  ram_boyutu == "32 GB" or  ram_boyutu == "64 GB" or  ram_boyutu == "128 GB" or ram_boyutu =="8" or ram_boyutu == "16" or ram_boyutu == "32" or ram_boyutu == "64" or ram_boyutu == "128"):
    print("Kuruluma Uygun")
else:
    print("Kuruluma Uygun Değil")