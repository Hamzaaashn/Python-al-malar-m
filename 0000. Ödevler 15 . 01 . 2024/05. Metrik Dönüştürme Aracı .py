def conversion(x) :
    conversion = x * 0.001
    return conversion

def printing(x,y) :
    print(y,x)


kilo = float(input("Kilonuzu Girin :\n"))
height = float(input("Boyunuzu Girin :\n"))

height_km = conversion(kilo)
kilo_gram = conversion(height)

printing("Boyunuz :\n",height_km)
printing("Kilonuz :\n",kilo_gram)