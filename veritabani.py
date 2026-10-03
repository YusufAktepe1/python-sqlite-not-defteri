from not_defteri import Defter

import sqlite3

class VeriTabaniYoneticisi:
    def __init__(self,db_adi="notlar.db"):
        self.baglanti=sqlite3.connect(db_adi)
        self.cursor = self.baglanti.cursor()

        self.tablo_olustur()


    def tablo_olustur(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                baslik TEXT NOT NULL,
                icerik TEXT NOT NULL,
                tarih TEXT
            )
        """)
        self.baglanti.commit()
    def not_ekle(self, baslik, icerik, tarih):
        self.cursor.execute("""
            INSERT INTO notlar (baslik, icerik, tarih) 
            VALUES (?, ?, ?)
        """, (baslik, icerik, tarih))  # Soru işaretleri ile parametreler execute parantezinin *içinde* olmalı!
        
        self.baglanti.commit()
        return "Başarılı: Not veritabanına kaydedildi."

    def notlari_listele(self):
        self.cursor.execute("SELECT * FROM  notlar")
        return self.cursor.fetchall()

    def not_guncelle(self,not_id,yeni_baslik,yeni_icerik):
        self.cursor.execute("""
            UPDATE notlar 
            SET baslik = ?, icerik = ? 
            WHERE id = ?
        """, (yeni_baslik, yeni_icerik, not_id))
        self.baglanti.commit()
        return f"Başarılı: {not_id} numaralı not güncellendi."

    def not_sil(self,not_id):
        self.cursor.execute("DELETE FROM notlar WHERE id = ?",(not_id,))
        self.baglanti.commit()
        return f" başarılı :{not_id} numarali not silindi"

    def baglanti_kapat (self):
        self.baglanti.close()
    
        
