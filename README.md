# class
![App Screenshot](https://github.com/firengizz099/class-OOP/blob/main/class.png?raw=true)
Bu Python kodu, Film, Kullanici, ve TeslaModelS sınıflarını içerir. Bu sınıflar, farklı nesne tiplerini temsil eden ve bu nesnelerin özelliklerini ve davranışlarını tanımlayan sınıflardır. İşte her bir sınıfın açıklamaları:

1) **Film Sınıfı**:

film_adi, yil, ve tur adında üç özellik (property) içerir.
__init__ metodu, bir film nesnesini başlatır ve film adı, yıl, ve tür bilgilerini alır.
Kullanici Sınıfı:

kullanici_adi, izlenen_filmler, ve onerilen_filmler adında üç özellik içerir.
__init__ metodu, bir kullanıcı nesnesini başlatır ve kullanıcı adını alır.
film_izle metodu, bir film nesnesini alır ve bu filmi kullanıcının izlediği filmler listesine ekler.
film_oner metodu, başka bir kullanıcıya bir film nesnesini önerir ve öneriyi diğer kullanıcının önerilen filmler listesine ekler.

2) **TeslaModelS Sınıfı**:
   
pil_kapasitesi, sarj_durumu, hiz, muzik, isiklar, ve sofor_uyku_durumu adında altı özellik içerir.
__init__ metodu, bir Tesla Model S nesnesini başlatır ve pil kapasitesi, şarj durumu, hız ve diğer bazı özellikleri alır.
muzik_ac metodu, arabanın müziğini açar, ancak şarj durumu belirli bir seviyenin altındaysa müzik açılmaz.
muzik_kapat metodu, arabanın müziğini kapatır.
trafik_isiklari_kontrol_et metodu, trafik ışıklarının durumuna göre aracın hızını ve davranışını kontrol eder.
trafik_isiklarini_degistir metodu, trafik ışıklarının durumunu değiştirir.
sofor_uyuku_durumu_kontrol metodu, şoförün uykusuzluk durumunu kontrol eder ve gerekirse mola verilmesi gerektiğini belirler.
durumu_goster metodu, arabanın mevcut durumunu ekrana basar.
Bu sınıflar, nesne yönelimli programlamada farklı nesne türlerini temsil etmek için kullanılabilir ve her bir sınıfın kendine özgü özellikleri ve davranışları vardır. Örneğin, Kullanici sınıfı kullanıcıların izlediği ve önerdiği filmleri takip etmek için kullanılabilir, TeslaModelS sınıfı ise bir elektrikli aracın özelliklerini ve davranışlarını modellemek için kullanılabilir.
