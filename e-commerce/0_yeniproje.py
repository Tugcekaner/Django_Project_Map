
# ! e-ticaret sitesi (bootstrap kullanacağız)

# ? 1. django-admin startproject newproject
# * komutu ile yeni projemizi oluşturuyoruz.

# ? 2. oluşturulan projenin klasörünü VSCode ile açıyoruz.
# * manage.py dosyası proje dışında açıkta kalacak şekilde yer almalı.
# * konum doğru olmazsa problem çıkacaktır.

# ? 3. py manage.py startapp user
# * komutu ile user application klasörünü oluşturuyoruz.
# * kullanıcı işlemleri bu bölümde yer alacak.

# ? 4. py manage.py startapp market
# * komutu ile market application klasörünü oluşturuyoruz.
# * ürün-market işlemleri bu bölümde yer alacak.

# ? 5. py manage.py migrate
# * komutu ile veritabanımızı oluşturuyoruz.

# ? 6. settings.py app ekleme
# * newproject/settings.py dosyasında ilk ayarları yapacağız.
# * settings.py dosyasındaki INSTALLED_APPS içine oluşturduğumuz applicationları ekleyeceğiz.
# * 'market',
# * 'user',

# ? 7. settings.py admin panel dil ayarı
# * LANGUAGE_CODE = 'en-us' satırını
# * türkçe panel için LANGUAGE_CODE = 'tr-tr' olarak değiştiriyoruz.

# ? 8. settings.py saat ayarı
# * TIME_ZONE = 'UTC' satırını
# * kullandığımız saat için TIME_ZONE = 'Turkey' olarak değiştiriyoruz.

# ? 9. templates klasörü
# * html dosyalarının yer alacağı klasörler.
# ? ilk yöntem
# * newproject içine templates adına bir klasör açıyoruz.
# ? ikinci yöntem
# * eğer applicationlar içinde html dosyalarımız daha okunaklı, toplu şekilde
# * dursun istiyorsak, appler içine birer templates klasörü açıyoruz.
# * newproject/settings.py içine tanıtmamız gerekli. Bunun için;
# * öncelikle boş bir satıra import os diyerek dosya yollarını oluşturabilmek için
# * gerekli os modülünü import ediyoruz.
# * ardından TEMPLATES bölümüne gelip 'DIRS' içine;
# * os.path.join(BASE_DIR, 'user', 'templates'),
# * os.path.join(BASE_DIR, 'market', 'templates'),
# * eklemelerini yaparak app içindeki templates klasörlerini tanıtıyoruz.

# ? 10. static klasörü
# * css,js,img dosyaları
# * newproject içine static klasörü açıyoruz
# * linklerken: /static/style.css (örnektir, pathi kontrol edin)
# * ya da {% static 'style.css' %} - jinja
# * sayfanın en başına {% load static %} - static dosyalarını yüklemesi için
# * newproject/settings içine (static kısmına) 
# * STATIC_URL = 'newproject/static/'
# * STATICFILES_DIRS =[BASE_DIR / 'newproject/static/']
# * ile static dosya yolunu belirliyoruz.
# * newproject/urls.py içine urlpatterns kapanışına
# * + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# * kodunu ekliyoruz. üst kısma da 
# * from django.conf.urls.static import static
# * from django.conf import settings
# * importlarını yaparak static dosyalarının okunmasını sağlıyoruz.

# ? 11. admin oluşturma
# * py manage.py createsuperuser 
# * komutu ile admin oluşturuyoruz.
# * şifre yazım kısmında terminalde şifre görünmeyecek lakin girilen şifreyi algılayacak.

# ? 12. urls.py içine app viewsleri eklemek
# * newproject/urls.py içine pathlerimizi yazacağız. 
# * Öncelikle applerin views dosyalarını tanıtmamız gerekli.
# * from market.views import *
# * from user.views import *
# * komutlarını girerek dosyaları tanıtıyoruz. Okunaklı olması için urlpatterns içerisinde
# * yorum satırlarıyla user ve market diye ayırabiliriz.


# ! Tebrikler! İlk projemizi oluşturduk!!