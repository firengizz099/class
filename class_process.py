from week3 import *


film1 = Film("Interstellar",2016,"Bilim Kurgu")
film2 = Film("Joker",2016,"Dram")
film3 = Film("Black Mirror", 2011, "Dram")

kullanici1 = Kullanici("Alice")
kullanici2 = Kullanici("Bob")

kullanici1.film_izle(film1)
kullanici1.film_izle(film2)
kullanici2.film_izle(film2)
kullanici2.film_izle(film3)

kullanici1.film_oner(kullanici2,film3)
kullanici2.film_oner(kullanici1,film1)

print(f"{kullanici1.kullanici_adi} tarfindan izlenen filmler: ")
for film in kullanici1.izlenen_filmler:
    print(film.film_adi)

print(f"{kullanici2.kullanici_adi} tarfindan izlenen filmler: ")
for film in kullanici2.izlenen_filmler:
    print(film.film_adi)

print(f"{kullanici1.kullanici_adi},{kullanici2.kullanici_adi} onerilen filmler: ")
for film in kullanici1.onerilen_filmler:
    print(film.film_adi)

print(f"{kullanici2.kullanici_adi},{kullanici1.kullanici_adi} onerilen filmler: ")
for film in kullanici2.onerilen_filmler:
    print(film.film_adi)

tesla = TeslaModelS(85)
tesla.muzik_ac()
tesla.trafik_isiklarini_degistir("Yesil")
tesla.trafik_isiklari_kontrol_et()
tesla.sofor_uyuku_durumu_kontrol("Uykusuz")
print("Bilgilendirme 5 saniye icinde kapanacak....")
time.sleep(5)
tesla.muzik_kapat()
tesla.durumu_goster()

import matplotlib.pyplot as plt
sarj_durumu = tesla.sarj_durumu
pil_kalan = 100 - sarj_durumu
labels = ["Saj EDilen", "Kalan"]
sizes = [sarj_durumu, pil_kalan]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels= labels, autopct = '%1.1f%%', startangle=90)
ax1.axis("equal")
plt.title(" Sarj Durumu Pasta Grafigi. ")
plt.show()


