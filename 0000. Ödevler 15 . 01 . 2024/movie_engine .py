import movie_main


while True :

    movie_main.show_menu()
    print()

    choose = input("Seçiminizi Yapın (1,2,3,4) :\n")
    if choose == "1" :
        movie_main.add_movie()

    elif choose == "2" :
        movie_main.show_movie_list()

    elif choose == "3" :
        movie_main.delete_movie()

    elif choose == "4" :
        movie_main.exit()
        break
    else :
        print("Kategoride Böyle Bir İşlem Bulunmuyor")