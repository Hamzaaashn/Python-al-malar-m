print("İzlemek İstediğinizin Yanındaki Sayıyı Yazın :\n")
tercih = input("1 : Sinema\n""2 : Tiyatro\n")

print("Öğrenci Misiniz ? \n")
öğrenim = input("Evet\n""Hayır\n")

if tercih == "1" :
    ücret = 15

    if öğrenim == "Evet":
        ücret -= ücret * 0.50
        print("Ödemeniz Gereken Ücret :\n",ücret)

    else:
        print("Ödemeniz Gereken Ücret :\n",ücret)

else:
    
    ücret = 10
    
    if öğrenim == "Evet":
        ücret -= ücret * 0.50
        print("Ödemeniz Gereken Ücret :\n",ücret)

    else:
        print("Ödemeniz Gereken Ücret :\n",ücret)