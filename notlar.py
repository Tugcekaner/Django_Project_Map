
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
