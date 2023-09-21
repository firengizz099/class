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

# import matplotlib.pyplot as plt
# sarj_durumu = tesla.sarj_durumu
# pil_kalan = 100 - sarj_durumu
# labels = ["Saj EDilen", "Kalan"]
# sizes = [sarj_durumu, pil_kalan]

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels= labels, autopct = '%1.1f%%', startangle=90)
# ax1.axis("equal")
# plt.title(" Sarj Durumu Pasta Grafigi. ")
# plt.show()

# import matplotlib.pyplot as plt
# # Yil ve yazilimci maaslari

# yillar = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
# maaslar = [60000,62000,64000,65000,66000,70000,75000,76000,77000,79000]

# plt.figure(figsize=(10,6))
# plt.plot(yillar,maaslar,marker='o',linestyle='-')
# plt.title("Yillara Gore yazilimci Maasi")
# plt.xlabel("Yil")
# plt.ylabel("Yillik Maas (USD)")
# plt.grid(True)
# plt.show()


# yillar = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
# maaslar = [60000,62000,64000,65000,66000,70000,75000,76000,77000,79000]

# plt.figure(figsize=(10,6))
# plt.bar(yillar,maaslar,color= "skyblue")
# plt.title("Yillara Gore yazilimci Maasi")
# plt.xlabel("Yil")
# plt.ylabel("Yillik Maas (USD)")
# plt.grid(axis='y')
# plt.show()


# kagegoriler = ['A','B','C','D']
# veriler = [25,30,40,45]

# plt.figure(figsize=(6,6))
# plt.pie(veriler,labels=kagegoriler,autopct='%1.1f%%',startangle=140)
# plt.title("Pasta Grafigi")
# plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
veri = [40,45,50,55,60,65]
sns.scatterplot(x=range(len(veri)), y=veri)
plt.title("Ornek Dagiklim Grafigi")
plt.xlabel("Sira")
plt.ylabel("Deger")
plt.show()

kagegoriler = ['A','B','C','D']
veriler = [25,30,40,45]

sns.barplot(x=kagegoriler, y=veriler, palette="viridis")
plt.title("Ornek Barplot Grafigi")
plt.xlabel("Kategori")
plt.ylabel("Deger")
plt.show()


data = [1,2,2,2,3,3,3,3,4,4,5,5,5,5]
sns.set(style="whitegrid")
sns.kdeplot(data,shade=True,alpha=1,color="purple")
plt.xlabel('Deger')
plt.ylabel('Yogunluk')
plt.title("Ornek KDE grafigi")
plt.show()

yas_data = [25,30,35,40,45,50,55,60,65]
diyabet_data = [0,1,0,1,0,1,0,1,0]

import pandas as pd
df = pd.DataFrame({'Yas':yas_data,"Diyabet":diyabet_data})
sns.set(style="whitegrid")
sns.kdeplot(data=df, x="Yas", hue="Diyabet",shade=True,common_norm=False,palette={0:"blue",1:"purple"})
plt.xlabel('Yas')
plt.ylabel('Yogunluk')
plt.title("Yasa Gore Diyabet yogunluk Grafigi ")
plt.show()
