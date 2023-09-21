class Film:
    def __init__(self, film_adi,yil,tur):
        self.film_adi = film_adi
        self.yil = yil
        self.tur = tur

class Kullanici:
    def __init__(self, kullanici_adi):
        self.kullanici_adi =kullanici_adi
        self.izlenen_filmler = []
        self.onerilen_filmler = []
    
    def film_izle(self, film):
        self.izlenen_filmler.append(film)
        print(f"{self.kullanici_adi}, {film.film_adi} filmini izledi..")
    
    def film_oner(self, kullanici, film):
        kullanici.onerilen_filmler.append(film)
        print(f"{self.kullanici_adi}, {kullanici.kullanici_adi}'ye {film.film_adi} filmini onerdi")


import time

class TeslaModelS:
    def __init__(self,pil_kapasitesi, sarj_durumu=50,hiz=0,muzik="Kapali"):
        self.pil_kapasitesi =pil_kapasitesi
        self.sarj_durumu =sarj_durumu 
        self.hiz = hiz
        self.muzik = muzik
        self.isiklar = "Kirmizi"
        self.sofor_uyku_durumu = "Uykusuz"

    def muzik_ac(self):
        if self.sarj_durumu > 20:
            self.muzik = "Acik"
            print("Muzik acildi")
        else:
            print("arabanin sarji cok dusuk, muzik acilmiyir! ")
    
    def muzik_kapat(self):
        self.muzik = "Kapali"
        print("Muzik kapatildi")

    def trafik_isiklari_kontrol_et(self):
        if self.isiklar == "Kirmizi":
            print("Trafik isgi kirmizi, arac duruyor.")
            self.hiz = 0
        elif self.isiklar == "Yesil":
            print("Trafik isgi yesil arac ilerliyor.")
        elif self.isiklar == "Sari":
            print("Trafik isiklari sari hazilikli olun. ")
        else:
            print("Gecersiz trafik isigi durumu.")
    
    def trafik_isiklarini_degistir(self, yeni_durum):
        self.isiklar = yeni_durum
        print(f" Trafik isiklari simdi {yeni_durum}")
    
    def sofor_uyuku_durumu_kontrol(self, sofor_uyuku_durumu):
        self.sofor_uyuku_durumu = sofor_uyuku_durumu
        if self.sofor_uyku_durumu == "Uykusuz":
            print("Sofor uykusuz gorunuyor  mola verilmeli")
        else:
            print("sofor uykusuz degil yolculuga devam.")
    
    def durumu_goster(self):
        print(f"Tesla Model S Bilgileri:"
              f"\nPil Kapasitesi: {self.pil_kapasitesi} kWh"
              f"\nSarj Durumu {self.sarj_durumu} % km/s"
              f"\nMuzik Durumu: {self.muzik}"
              f"\nSofor uyku Durumu:{self.sofor_uyku_durumu}" )












