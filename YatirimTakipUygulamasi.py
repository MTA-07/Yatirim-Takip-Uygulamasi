yatirimlar = []

while True:
    print("******* Yatirim Takip Uygulamasi *******")
    print("1 - Yapilan Yatirim Tutari (Yatirim Ekleme)")
    print("2 - Yapilan Yatirimlari Listele")
    print("3 - Yapilan Yatirima Gore Toplam Gosterme")
    print("4 - Cikis")

    secim = int(input("Lutfen Seciminizi Giriniz: "))

    if secim == 1:
        kategori = input("Neye Yatirim Yaptiniz?: ")
        tutar = float(input("Yapilan Yatirim Tutarini Giriniz: "))
        tarih = input("Tarih (gun/ay/yil): ")

        yatirim = {
            "kategori": kategori,
            "tutar": tutar,
            "tarih": tarih
        }

        yatirimlar.append(yatirim)
        print("Yaptiginiz Yatirim Eklendi")

    elif secim == 2:
        print("******* Yapilan Yatirimlarin Listesi *******")
        for m in yatirimlar:
            print(f"{m['tarih']} | {m['kategori']} | {m['tutar']}")

    elif secim == 3:
        yatirim_ara = input("Yatirim Yapilan Seyin Ismi: ")
        toplam = 0

        for m in yatirimlar:
            if m["kategori"] == yatirim_ara:
                toplam += m["tutar"]

        print(f"{yatirim_ara} adli varliğa yapilan toplam yatirim: {toplam}")

    elif secim == 4:
        print("Bitti mi hikayemiz, bu ne bicim son boyle?")
        break

    else:
        print("Gecersiz secim yaptin canim")


