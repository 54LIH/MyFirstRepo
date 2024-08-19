import random  # Rastgele seçimler için kullanıyoruz.


def tas_kagit_makas_Salih_Akca():
    print("Hazır mısın! Dünyanın en ünlü oyunlarından birini oynayacağız!\n"
          "Taş, Kağıt, Makas!\n"
          "3 tur oynayacağız ve 2 tur kazanan oyunu kazanır.\n"
          'Oynamak için "Taş", "Kağıt" veya "Makas" yaz, ya da oyundan çıkmak istersen "Çıkış" yaz.\n'
          "Oyun BAŞLIYOR!")

    oyun_numarasi = 1  # Oyun numarası
    while True:  # Sonsuz döngü, oyun bitene kadar devam eder.

        oyuncu_skoru = 0  # Oyuncu skoru
        bilgisayar_skoru = 0  # Bilgisayar skoru
        tur_numarasi = 1  # Tur numarası

        # Oyuncu veya bilgisayar 2 tura ulaşana kadar döngü devam eder
        while oyuncu_skoru < 2 and bilgisayar_skoru < 2:
            print(f"\n### OYUN {oyun_numarasi}, TUR {tur_numarasi}! : #####")

            oyuncu_secim = input("Taş, Kağıt, Makas veya çıkış? : ").lower()

            if oyuncu_secim == "çıkış":
                print("Oyunu oynamak istemiyorsan neden fonksiyonu çağırdın ki?\n"
                    "Gerçekten oynamak istediğinizde ben yine burada olacağım!")
                return  # Oyunu bitirir

            if oyuncu_secim not in ["taş", "kağıt", "makas"]:
                print("Geçersiz seçim! Tekrar dene. Taş, kağıt ya da makas, birini  yaz!")
                continue  # Geçersiz seçimde döngü başa döner

            bilgisayar_secim = random.choice(["taş", "kağıt", "makas"])
            print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

            # Oyuncu ve bilgisayar seçimlerini karşılaştırma
            if oyuncu_secim == bilgisayar_secim:
                print("Bu tur berabere! Yoksa zihnini mi okudum. Makinalar insanların zihnini mi okuyor...\n"
                      "Şaka yaptım :) zaten üç ihtimal var.")
            elif (oyuncu_secim == "taş" and bilgisayar_secim == "makas") or \
                    (oyuncu_secim == "kağıt" and bilgisayar_secim == "taş") or \
                    (oyuncu_secim == "makas" and bilgisayar_secim == "kağıt"):
                print("Şanslısın! Aslında SADECE şanslısın.\n"
                      "Bu turu sen kazanmış olabilirsin... veya kazanmışsındır...\n"
                      "Tamaaam sen kazandın.")
                oyuncu_skoru += 1
            else:
                print("Bu turu kaybettin. Yapay zeka işimi elimden alacak mı diye düşünüyordun dimi bak gerçek oluyor...\n"
                    "Şaka şaka bu sadece kural tabanlı, rasgele seçim yapan bir algoritmanın işi :) ")
                bilgisayar_skoru += 1

            print(f"Skor - Oyuncu: {oyuncu_skoru}, Bilgisayar: {bilgisayar_skoru}")

            tur_numarasi += 1  # Her tur sonrası tur numarasını artırır.

        # Oyun sonucuna göre mesaj
        if oyuncu_skoru == 2:
            print("Oyunu kazandın! Yeniden oynamak ister misin, şampiyon? (Evet/Hayır)")
        else:
            print("Bilgisayar oyunu kazandı! Yeniden oynamak ister misin? (Evet/Hayır)")

        # Oyuncuya tekrar oynamak isteyip istemediğini soruyoruz.
        yeniden_oyna = input().lower()

        if yeniden_oyna == "evet":
            oyun_numarasi += 1  # Oyun numarası artar ve yeni bir oyun başlar.
        else:
            print("Oynadığınız için teşekkürler!")
            break  # Oyun sona erer


# Oyunu başlatıyoruz
tas_kagit_makas_Salih_Akca()
