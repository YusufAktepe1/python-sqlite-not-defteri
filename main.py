from veritabani import VeriTabaniYoneticisi

# Veritabanı yöneticimizi başlatıyoruz
db_y = VeriTabaniYoneticisi()

while True:
    print("""
        --- DİJİTAL NOT DEFTERİ ---
    1. Not Ekle
    2. Notları Listele
    3. Not Güncelle
    4. Not Sil
    5. Çıkış
    """)
    
    secim = input("Seçiminiz (1-5): ")

    if secim == "1":
        baslik = input("Not Başlığı: ")
        icerik = input("Not İçeriği: ")
        tarih = input("Tarih (Örn: 2026-06-06): ")
        
        sonuc = db_y.not_ekle(baslik, icerik, tarih)
        print(f"\n{sonuc}")

    elif secim == "2":
        notlar = db_y.not_listele() if hasattr(db_y, 'not_listele') else db_y.notlari_listele()
        print("\n--- KAYITLI NOTLAR ---")
        if not notlar:
            print("Henüz kaydedilmiş bir not yok.")
        else:
            for not_item in notlar:
                # Veritabanından gelen format: (id, baslik, icerik, tarih)
                print(f"ID: {not_item[0]} | Başlık: {not_item[1]} | Tarih: {not_item[3]}")
                print(f"İçerik: {not_item[2]}")
                print("-" * 30)

    elif secim == "3":
        not_id = input("Güncellenecek Notun ID numarası: ")
        yeni_baslik = input("Yeni Başlık: ")
        yeni_icerik = input("Yeni İçerik: ")
        
        sonuc = db_y.not_guncelle(not_id, yeni_baslik, yeni_icerik)
        print(f"\n{sonuc}")

    elif secim == "4":
        not_id = input("Silinecek Notun ID numarası: ")
        sonuc = db_y.not_sil(not_id)
        print(f"\n{sonuc}")

    elif secim == "5":
        print("\nProgramdan çıkılıyor. Notlarınız veritabanında güvende! Görüşmek üzere 👋")
        break
    else:
        print("\n[!] Geçersiz seçim yaptınız. Lütfen 1 ile 5 arasında bir sayı girin.")