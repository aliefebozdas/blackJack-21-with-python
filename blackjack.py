import random
kartlar = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
           "papaz", "papaz", "papaz", "papaz", "kız", "kız", "kız", "kız", "vale", "vale", "vale", "vale", "as", "as", "as", "as"]
devamMi = True
devamMi2 = True
toplam = 0
deger = 0

kartlarim = []


def kart_cek():
    rastgele_cek = random.randint(0, 51)
    if(rastgele_cek >= 36 and rastgele_cek <= 47):
        cek_deger = 10

    elif(rastgele_cek > 47):
        cek_deger = 11

    else:
        cek_deger = kartlar[rastgele_cek]

    return cek_deger


def pc_karari():
    pc_devamMi = True
    pc_deger = 0
    toplam_pc = 0
    pc_kartlari = []
    for i in range(2):
        pc_rastgele = random.randint(0, 51)
        if (pc_rastgele >= 36 and pc_rastgele <= 47):
            pc_deger = 10
            toplam_pc += pc_deger
        elif (pc_rastgele > 47):
            pc_deger = 11
            toplam_pc += pc_deger
        else:
            pc_deger = kartlar[pc_rastgele]
            toplam_pc += pc_deger
        pc_kartlari.append(kartlar[pc_rastgele])
    while pc_devamMi:
        if (toplam_pc <= 16):
            pc_yeni_kart = kart_cek()
            pc_kartlari.append(pc_yeni_kart)
            toplam_pc += pc_yeni_kart
        else:
            pc_devamMi = False
    print("PC kartlarını açtı..")
    print("Bilgisayarın Kartları= {0}", format(pc_kartlari))

    pc_kartlari.clear()
    return toplam_pc


while devamMi:
    print("Black Jack Oyunumuza Hoşgeldiniz ...")
    print("***Menü***")
    print("1- Nasıl Oynanır ?")
    print("2- Oyuna Başla ")
    print("3- Çıkış Yap ")
    ana_islem = int(input("İşleminizi Seçiniz :"))
    devamMi2 = True
    devamMi3 = True
    if (ana_islem == 1):
        print("Bilgisayar size otomatik olarak 2 kart verecektir. Aldığınız kartların toplamı 21 veya 21'e yakın olması hedeftir.")
        print("Eğer 21'e çok uzaksanız bir kart daha çekebilirsiniz. Sizle birlikte bilgisayarda oynuyor olacak. Hanginiz şanslıysa o   turu kazanacak. Eğer aldığınız kartla beraber 21'i geçerseniz kaybedersiniz. ")
        geri_gel = int(input("Geri gelmek için 1'e basınız.."))
        if (geri_gel == 1):
            print("Geri geldiniz..")
        else:
            print("Çıktınız..")
            devamMi = False
    elif (ana_islem == 2):

        for i in range(2):
            rastgele = random.randint(0, 51)
            if (rastgele >= 36 and rastgele <= 47):
                deger = 10
                toplam += deger
            elif (rastgele > 47):
                deger = 11
                toplam += deger
            else:
                deger = kartlar[rastgele]
                toplam += deger
            kartlarim.append(kartlar[rastgele])
        print("Kartım= {0}", format(kartlarim))
        while devamMi3:
            hamle = input(
                "Hamlenizi Yapınız : Kart çekmek istiyor musunuz : E/H :")
            if(hamle == "E" or hamle == "e"):
                yeni_kart = kart_cek()
                kartlarim.append(yeni_kart)
                toplam += yeni_kart
                print(kartlarim)

            elif(hamle == "H" or hamle == "h"):
                print("Kartlarınızı açtınız..")
                print(kartlarim)
                print(toplam)
                devamMi3 = False

            else:
                print("Geçerli bir değer giriniz ..")
                break
        pc_toplam = pc_karari()
        if toplam > 21 and pc_toplam <= 21:
            print("Kartların Toplamı 21 Sayısını Geçmemeli !! Kaybettiniz !!")
        elif toplam > 21 and pc_toplam > 21:
            print("Bilgisayarla birlikte kaybettiniz !! Berabere sayılırsınız :)")
        elif toplam <= 21 and pc_toplam > 21:
            print("Pc 21 sayısını geçti, Kazandınız !! Tebrikler !!")
        elif toplam > pc_toplam:
            print("Tebrik Ederiz !! Kazandınız !!")
        elif toplam == pc_toplam:
            print("Pc ile berabere Kaldınız !!")
        else:
            print("Bilgisayar Kazandı !! Siz Kaybettiniz :)")
        toplam = 0
        kartlarim.clear()
        while devamMi2:
            print("Geri Gelmek istiyorsanız 1'den başka tuşa basınız..")
            devamMi3 = True
            islem = int(input("Bir daha oynamak istiyorsanız 1'e basınız.."))
            if (islem == 1):
                for i in range(2):
                    rastgele = random.randint(0, 51)
                    if (rastgele >= 36 and rastgele <= 47):
                        deger = 10
                        toplam += deger
                    elif (rastgele > 47):
                        deger = 11
                        toplam += deger
                    else:
                        deger = kartlar[rastgele]
                        toplam += deger
                    kartlarim.append(kartlar[rastgele])
                print("Kartım= {0}", format(kartlarim))

                while devamMi3:
                    hamle = input(
                        "Hamlenizi Yapınız : Kart çekmek istiyor musunuz : E/H :")
                    if(hamle == "E" or hamle == "e"):
                        yeni_kart = kart_cek()
                        kartlarim.append(yeni_kart)
                        toplam += yeni_kart
                        print(kartlarim)

                    elif(hamle == "H" or hamle == "h"):
                        print("Kartlarınızı açtınız..")
                        print(kartlarim)
                        print(toplam)
                        devamMi3 = False
                    else:
                        print("Geçerli bir değer giriniz ..")
                        break
                pc_toplam = pc_karari()
                if toplam > 21 and pc_toplam <= 21:
                    print("Kartların Toplamı 21 Sayısını Geçmemeli !! Kaybettiniz !!")
                elif toplam > 21 and pc_toplam > 21:
                    print(
                        "Bilgisayarla birlikte kaybettiniz !! Berabere sayılırsınız :)")
                elif toplam <= 21 and pc_toplam > 21:
                    print("Pc 21 sayısını geçti, Kazandınız !! Tebrikler !!")
                elif toplam > pc_toplam:
                    print("Tebrik Ederiz !! Kazandınız !!")
                elif toplam == pc_toplam:
                    print("Pc ile berabere Kaldınız !!")
                else:
                    print("Bilgisayar Kazandı !! Siz Kaybettiniz :)")
                toplam = 0
                kartlarim.clear()
            else:
                print("Geri Geldiniz..")
                devamMi2 = False
    elif (ana_islem == 3):
        print("Çıkış Yaptınız..")
        devamMi = False
    else:
        print("Başka bir değer giriniz !!")
