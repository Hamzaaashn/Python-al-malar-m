questions = [
            {"Question" : "Hangi Renk Trafik Lambasının Ortasında Yer Alır ? :",
                "Options " : ["A) Kırmızı", "B) Sarı" , "C) Yeşil","D) Mavi"] ,
                "Correct Answer" :"C"},

           {"Question" : "Hangi Gezegen Güneş Sistemi 'ndeki En Büyük Gezegendir ? :" ,
                "Options " : ["A) Mars " , "B) Jüpiter" , "C) Venüs", "D) Satürn"],
                "Correct Answer" : "B"},

           {"Question" : "Türkiyenin En Büyük Şehri Nedir ? :" ,
                "Options " : [ "A) İstanbul ", "B) Ankara ", "C) Sivas ","D) Konya "] ,
                "Correct Answer" :"D"},

           {"Question" : "Albert Einstein hangi alanda Nobel ödülü almıştır? :",
                "Options " : ["A) Fizik ","B) Kimya ","C) Tarih ", "D) Astronomi"], 
                "Correct Answer" : "A"},

           {"Question" : "Harita biliminin diğer adı nedir ? :" ,
                "Options " : [ "A) Filoloji " , "B) Kartogrofya " , "C) Epigrafi ","D) Liloloji "],
                "Correct Answer" : "B"},

           {"Question" : "Divan edebiyatında padişahları ve devletin ileri gelenleri övmek için yazılan methiye türündeki şiirlere ne ad verilir ? " ,
                 "Options " : ["A) Destan ", "B) Divan ","C) Anı ","D) Kaside "],
                "Correct Answer" :"D"},

           {"Question" : "Kırmızı ve sarı renklerinin karışımından hangi renk elde edilir ? :",
                "Options " : ["A) Ela " , "B) Turuncu ","C) Lacivert ","D) Yeşil "],
                "Correct Answer" : "B"},

           {"Question" : "Yüz ölçümü bakımından en büyük ülke hangisidir ? :" ,
                "Options" : ["A) T Ü R K İ Y E  ","B) Rusya " , "C) İngiltere ","D) Şili "] , 
                "Correct Answer" : "B"},

           {"Question" : "Araçların şehir içinde daha yavaş gitmesini sağlamak için yollarda kullanılan tümseklere ne ad verilir ? :" ,
                "Options " : ["A) Kasis " , "B) Kavşak ", "C) Yaya Geçidi ", "D) Alt Geçit " ],
                "Correct Answer" : "A"},

           {"Question" : "Nüfusu sadece 825 olan, en küçük Avrupa ülkesi hangisidir ? ", 
                "Options" : ["A) Norveç ", "B) İspanya ", "C) İtalya ","D) Vatikan "] , 
                "Correct Answer" : "D"}]


total_correct_answer = 0
for question in questions :
    print(question , "Question")
    answer = input(questions["Options"])


    if answer == questions["Correct Answer"] :
        print("Tebrikler ! Doğru Cevap")
        total_correct_answer += 1
        continue


    print("Malesef Hatalı Cevap Verdiniz")
    print("Toplam",total_correct_answer, "Adet Doğru Cevap Verdiniz")