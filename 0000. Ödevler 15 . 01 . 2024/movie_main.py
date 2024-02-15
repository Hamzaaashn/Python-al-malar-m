print_movie ={}

def show_menu():

    print(" 1- Film Ekleme\n",
          "2- Film Listesini Göster\n",
          "3- Film Sil\n",
          "4- Uygulamadan Çıkış")
    

def add_movie():
    movie_name = input("Filmin Adını Girin :\n")
    movie_director = input("Filmin Yönetmenini Girin :\n")
    movie_year = input("Filmin Çıkış Yılını Girin :\n")

    print_movie[movie_name] = {"Filmin Yönetmeni" : movie_director ,  "Filmin Çıkış Yılı" : movie_year}
    print(movie_name , "Filmi Eklendi")

def show_movie_list() :
    print(print_movie)
    movie_name = input("Gösterilecek Filmin Adını Girin :\n")

    if movie_name in print_movie :
        material = print_movie[movie_name]
        print(movie_name, "Filminin Bilgileri :\n")
        print("Filmin Adı :",movie_name)
        print("Filmin Yönetmeni :",material["Filmin Yönetmeni"])
        print("Filmin Çıkış Yılı :", material["Filmin Çıkış Yılı"])
    else :
        print("Böyle Bir Film Bulunamadı :(")


def delete_movie() :
    movie_name = input("Silinecek Filmin Adını Girin :\n")

    del print_movie[movie_name]
    print(movie_name,"Filmi Listeden Kaldırılıyor ...")


def exit() :
    print("Uygulamamızı Kullandığınız İçin Teşekkürler")
    print("Uygulamadan Çıkış Yapılıyor ...")