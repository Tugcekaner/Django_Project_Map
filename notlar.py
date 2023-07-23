
# ! NOTLAR

# ? Django nedir?
# * Django, Python programlama dili ile yazılmış açık kaynaklı ve yüksek düzeyde verimli bir web çerçevesidir. 
# * Web uygulamaları ve siteleri geliştirmeyi kolaylaştıran, modüler, güçlü ve hızlı bir altyapı sağlar. 
# * Django, web geliştiricilerinin uygulamalarını hızlı bir şekilde oluşturmalarına, bakım yapmalarına ve 
# * ölçeklendirmelerine olanak tanır.
# * Django'nun özellikleri şunlardır:
# * 1. Şablonlama Sistemi: Django, veritabanından alınan verileri dinamik olarak HTML şablonlarıyla birleştirerek 
# * dinamik içerik oluşturmayı sağlar.
# * 2. ORM (Object-Relational Mapping): Django, veritabanı tablolarını Python sınıfları olarak temsil ederek, 
# * veritabanı işlemlerini sadece Python koduyla gerçekleştirmenizi sağlar.
# * 3. URL Yönlendirmesi: Django, URL yapılandırmasını ve istemcilere verilen URL'lere nasıl cevap vereceğini 
# * kolayca tanımlamanıza olanak tanır.
# * 4. Admin Arayüzü: Django, veritabanı tablolarını düzenlemek, eklemek ve silmek için hazır bir yönetim arayüzü sunar.
# * 5. Güvenlik: Django, otomatik olarak birçok güvenlik önlemi alır ve kullanıcı kimlik doğrulaması, form doğrulama ve 
# * güvenli çerez yönetimi gibi güvenlik konularını kolaylaştırır.
# * 6. Otomatik Yönetim: Django, yönetimi kolaylaştırmak için otomatik olarak yaratılmış yönetim paneli ve araçları sağlar.
# * 7. Dökümantasyon ve Topluluk: Django, kapsamlı dökümantasyonu ve aktif bir topluluğu ile geliştiricilere destek verir.
# * Django, ölçeklenebilir ve esnek bir yapıya sahiptir, bu nedenle küçük bloglardan büyük web sitelerine kadar 
# * çeşitli proje türlerine uygun bir seçenektir. Django, basit ve hızlı uygulama geliştirmeye odaklanarak, 
# * web geliştirme sürecini verimli hale getirmeyi amaçlar.

# ? Django urlleri;
# * http://127.0.0.1:8000 - site
# * http://127.0.0.1:8000/admin/ - admin panel


# ? jinja 
# * Jinja, Python programlama diline özgü bir şablon motorudur. 
# * Jinja, Python dilinin gücünü ve esnekliğini şablonlama için kullanılabilir hale getirir. 
# * Django gibi popüler Python web çerçevelerinde ve Flask gibi mikro web çerçevelerinde 
# * yaygın olarak kullanılmaktadır.
 
# ? block
# * {% block blockname %}  {% endblock blockname %}
# * başka sayfalarda düzenlemek/değiştirmek istediğimiz bölümler için kullanıyoruz.

# ? includes
# * {% include 'includes/_navbar.html' %}
# * componentları include etmek, sayfaya aktarmak için kullanıyoruz.

# ? extends
# * {% extends 'base.html' %}
# * ortak iskeletimizi sayfaya aktarmak için kullanıyoruz.
# * Tüm sayfalarda tekrar tekrar html iskeleti oluşturmak zorunda kalmayalım,
# * bir değişiklik yapacağımızda tüm sayfalarda tek tek yapmayalım diye. Kontrolü çok kolaylaştırıyor.

# ? csrf token
# * Django'da {% csrf_token %} şablon etiketi, Cross-Site Request Forgery (CSRF) saldırılarına karşı 
# * koruma sağlamak için kullanılır. CSRF saldırıları, kötü niyetli kullanıcıların, yetkili bir kullanıcının 
# * tarayıcısını kullanarak istenmeyen işlemleri gerçekleştirmesini amaçlayan saldırılardır. 
# * Django, varsayılan olarak tüm POST isteklerinde CSRF koruması sağlar.
# * {% csrf_token %} şablon etiketi, Django web uygulamanızda POST isteği yapan bir form oluştururken 
# * kullanmanız gereken bir güvenlik önlemidir. Bu etiket, formun içinde yer almalıdır.

# ? form methodu olarak POST ve GET
# * Form metodları GET ve POST, web formlarının sunucuya veri gönderme şeklini belirler. 
# * Temel farklar şunlardır:
# ! Veri İletme Yolu:
# * GET: Veriler, URL'nin bir parçası olarak sunucuya iletilir. Kullanıcıların bu verilere kolayca erişmesi ve 
# * paylaşması mümkündür. Örneğin, bir arama sorgusu www.example.com/search/?q=your_query şeklinde gönderilir.
# * POST: Veriler, HTTP isteğinin gövdesinde gizli bir şekilde sunucuya iletilir. URL'de görünmezler ve 
# * kullanıcılar tarafından kolayca görüntülenemez veya değiştirilemez.
# ! Veri Boyutu: 
# * GET: Sınırlı veri boyutları için uygundur. Genellikle 2048 karakterlik (tarayıcı ve sunucu tarafından 
# * kabul edilen farklı değerler olabilir) bir URL uzunluğu sınırı vardır. Bu nedenle büyük veri kümesi 
# * göndermek için uygun değildir.
# * POST: GET yöntemine kıyasla daha büyük veri boyutları göndermek için uygun bir seçenektir. 
# * Sunucu ve tarayıcı tarafından belirlenen maksimum boyut sınırları vardır, ancak genellikle GET yöntemine 
# * kıyasla daha yüksektir.
# ! Veri Güvenliği: 
# * GET: Veriler URL'de açıkça göründüğü için, hassas bilgilerin GET yöntemiyle gönderilmesi önerilmez. 
# * Örneğin, kullanıcı adları, parolalar veya diğer hassas bilgiler GET ile gönderilmemelidir, 
# * çünkü bu bilgiler tarayıcı geçmişine veya sunucu loglarına kaydedilebilir.
# * POST: Veriler gizli olarak gönderildiğinden, POST yöntemi hassas bilgilerin güvenli bir şekilde 
# * sunucuya iletilmesi için daha uygundur.
# ! Caching (Önbellekleme) Davranışı: 
# * GET: Tarayıcılar, GET isteklerini önbellekleme eğilimindedirler, bu nedenle aynı GET isteği tekrar 
# * gönderildiğinde önbellekteki sonuçları döndürme olasılığı yüksektir.
# * POST: Tarayıcılar, POST isteklerini önbellekleme eğiliminde değildir, bu nedenle her zaman sunucuya 
# * yeni bir POST isteği gönderir.
# ! İşlemlerin Yan Etkileri: 
# * GET: GET istekleri, sunucuda herhangi bir veri değişikliği yapmamalıdır. Yani, bu tür istekler 
# * genellikle okuma işlemleri için kullanılır ve sunucuda herhangi bir veri değişikliği olmamalıdır.
# * POST: POST istekleri, sunucuda veri eklemek, güncellemek veya silmek gibi işlemler yapabilir. 
# * Yani, bu tür istekler veri değişikliklerinde kullanılır.
# * Sonuç olarak, veri göndermek için GET ve POST metodları farklı amaçlara hizmet eder ve 
# * her birinin belirli kullanım durumları vardır. Genel olarak, hassas verileri 
# * (örneğin kullanıcı adı ve parolalar) göndermek için POST yöntemi tercih edilirken, sadece veri almak veya 
# * arama sorguları gibi veri göndermek için GET yöntemi kullanılabilir.

# ? Django linklemeler
# * urls.py Dosyası: Django projesi ve uygulamalarındaki urls.py dosyalarında URL tanımlarını yaparsınız.
# * urlpatterns Listesi: urls.py dosyasında urlpatterns listesi, tüm URL tanımlarını içeren bir liste olmalıdır. 
# * Bu listedeki her bir öğe, bir URL tanımı ve ilişkili görüntüleme işlevini belirtir.
# * URL Parametreleri: Django'da URL'lere parametreler eklemek için çeşitli yollar vardır. 
# * Örneğin, bir URL'de belirli bir nesnenin kimliğini veya diğer bilgileri taşımak için parametreler kullanılabilir.
# * Link Oluşturma: reverse() fonksiyonu veya {% url %} etiketi kullanılarak linkler oluşturulabilir. 
# * Bu yöntemler, URL yapılarını değiştirdiğinizde tüm linklerin otomatik olarak güncellenmesini sağlar.


