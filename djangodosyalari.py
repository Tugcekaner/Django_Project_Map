
# ! DJANGO DOSYALARI VE İŞLEVLERİ

# ? init.py
# * __init__.py dosyası, bir Python paketini (bir dizin içindeki Python modüllerinin toplamını)
# * tanımlamak için kullanılır. Django uygulamaları ve Django projeleri, Python paketleri 
# * olarak kabul edilir, bu nedenle her bir uygulama ve projenin kendi içinde 
# * __init__.py dosyası bulunur.

# ? asgi.py
# * ASGI sunucuları, Django projelerine daha fazla esneklik ve performans sağlamak için 
# * kullanılabilir. Özellikle, WebSocket bağlantıları, uzun süreli arka plan işlemleri 
# * ve asenkron görüntü işleme gibi gerçek zamanlı işlemler, ASGI aracılığıyla daha iyi 
# * bir şekilde desteklenir. Ayrıca, Django Channels kütüphanesi ile birleştirilerek, 
# * Django projeleri asenkron özelliklere sahip WebSocket uygulamaları ve 
# * canlı bildirimler gibi özellikleri kolayca geliştirmeye olanak tanır.
# * Özetle, asgi.py dosyası, Django projelerinin ASGI sunucuları ile etkileşime girebilmesini 
# * ve asenkron özelliklerden yararlanabilmesini sağlar. Ancak, çoğu basit Django projesi için 
# * gerekli değişiklikler otomatik olarak yapıldığından, bu dosyayla genellikle doğrudan 
# * etkileşimde bulunmanız gerekmez.

# ? settings.py
# * settings.py, Django projelerinin temel yapılandırma ve ayarlarını içeren Python dosyasıdır. 
# * Django'nun temel yapılandırma dosyasıdır ve projenin davranışını ve özelliklerini kontrol 
# * etmek için kullanılır. Bu dosya, projenin kök dizininde bulunur ve Django projesinin 
# * tüm ayarlarının tanımlandığı merkezi bir yerdir.

# ? wsgi.py
# * wsgi.py, Django projelerinin WSGI (Web Server Gateway Interface) sunucuları tarafından 
# * kullanılan WSGI uygulamasının tanımlandığı Python dosyasıdır. 
# * Django, WSGI standartlarını kullanarak web sunucularıyla etkileşime geçerek 
# * web uygulamalarını çalıştırır.
# * WSGI, Python web uygulamalarının standart bir şekilde web sunucularıyla iletişim kurmasına 
# * olanak tanır. Bu sayede Django ve diğer Python web çerçeveleri, 
# * farklı web sunucu yazılımlarıyla uyumlu çalışabilir. 
# * Django'nun WSGI desteği sayesinde uygulamanızı Apache, Nginx, Gunicorn, uWSGI gibi farklı 
# * WSGI uyumlu sunucularda çalıştırabilirsiniz.

# ? urls.py
# * urls.py, Django projelerindeki URL yapılandırmasını yönetmek için kullanılan 
# * Python dosyasıdır. Django'nun temel yönlendirme sistemi, gelen HTTP isteklerini 
# * doğru view (görünüm) fonksiyonlarına yönlendirmek ve bu görünümlerden dönen cevapları 
# * kullanıcılara göndermek için URL yapılandırmasını kullanır.
# * Django uygulamaları, genellikle bir veya daha fazla urls.py dosyasına sahiptir. 
# * Bir Django projesinin ana urls.py dosyası, projenin kök dizininde bulunur ve 
# * projedeki tüm uygulamaların URL yapılandırmalarını yönlendirir. Aynı zamanda, 
# * her uygulamanın kendi urls.py dosyası da olabilir ve bu dosya, 
# * uygulamaya özgü URL yapılandırmasını tanımlar.

# ? views.py
# * views.py, Django projelerinde HTTP isteklerini işleyen ve HTTP cevaplarını döndüren 
# * Python dosyasıdır. Django'da "view" kavramı, kullanıcıların tarayıcılarından gönderdikleri 
# * HTTP isteklerini ele alan işlevleri ifade eder. Bu işlevler, gelen isteğe uygun olarak 
# * bir şablon (HTML dosyası) veya JSON verisi gibi cevapları oluşturur ve 
# * kullanıcılara geri gönderir.
# * views.py dosyasında tanımlanan her bir işlev (view) bir HTTP isteğine yanıt verir ve 
# * bu işlevler Django projenizde belirli bir URL deseni ile eşleştirilir. 
# * Bu, Django'nun URL yapılandırmasını urls.py dosyasında yapılandırılarak gerçekleştirilir.

# ? models.py
# * models.py, Django projelerinde veritabanı tablolarını ve veri yapısını tanımlamak için 
# * kullanılan Python dosyasıdır. Django'nun MVC (Model-View-Controller) mimarisine dayanan 
# * MTV (Model-Template-View) mimarisinde "Model" katmanını temsil eder.
# * Bu dosya, Django'nun "Model" bileşeninin kalbidir ve Django ORM (Object-Relational Mapping)
# * ile etkileşime girerek veritabanı tablolarını oluşturmak, sorgulamak ve 
# * verileri manipüle etmek için kullanılır.

# ? admin.py
# * admin.py, Django projelerinde Django admin arayüzü için yapılandırma dosyasıdır. 
# * Django admin arayüzü, projedeki veritabanı tablolarını düzenlemek, eklemek, silmek ve 
# * sorgulamak için kullanılan hazır bir yönetim arayüzüdür. Bu arayüz, 
# * projenizi geliştirme ve içerik yönetimi süreçlerini kolaylaştırmak için kullanılabilir.
# * admin.py dosyasında, Django'nun admin arayüzünde hangi modellerin görüntüleneceği, 
# * nasıl düzenleneceği, hangi alanların görüntüleneceği ve sıralanacağı gibi ayarlar yapılır.

# ? forms.py
# * forms.py, Django projelerinde kullanıcıların web formları aracılığıyla veri göndermelerini 
# * ve bu verileri işlemek için kullanılan Python dosyasıdır. 
# * Django'nun form yapısını tanımlamak için kullanılır.
# * Web formları, kullanıcıların veri girişi yapmasını ve bu verilerin sunucuya gönderilmesini 
# * sağlayan arayüz elemanlarıdır. Django, web formlarını oluşturmayı ve bu formlardan 
# * gelen verileri işlemeyi kolaylaştıran bir form API'si sağlar. Bu işlevselliğe forms.py 
# * dosyası aracılığıyla ulaşılır.
# * forms.py dosyasında, kullanıcı girişi yaparken doğrulama kuralları ve veri manipülasyonu 
# * gibi form işlevleri tanımlanır. Django, form alanlarını ve doğrulama kurallarını 
# * temsil eden hazır sınıflar sağlar. Bu sınıflar, HTML formları oluşturmak ve 
# * kullanıcı verilerini işlemek için kullanılabilir.

# ? tests.py
# * tests.py, Django projelerinde otomatik testleri tanımlamak için kullanılan Python dosyasıdır. 
# * Django, yazılımın doğru çalıştığını doğrulamak ve gelecekteki değişikliklerin mevcut işlevselliği 
# * bozmadığından emin olmak için testleri yazmayı teşvik eder. Testler, uygulamanın kodunun doğru ve 
# * beklenen sonuçları ürettiğini kontrol etmek için kullanılır.
# * tests.py dosyasında tanımlanan testler, Django'nun test çerçevesini kullanarak otomatik olarak 
# * çalıştırılabilir. Bu testler, projedeki model, view (görünüm) ve diğer işlevleri test etmek için 
# * kullanılabilir. Testler, veritabanına erişmeden, gerçek HTTP istekleri yapmadan ve 
# * gerçek web sunucuları kullanmadan kodun işleyişini kontrol edebilir.
# * Django'nun test çerçevesi, test işlevleri tanımlamanızı ve bu işlevleri belirli durumlar için 
# * beklenen sonuçlarla karşılaştırmanızı sağlar. Testler, hata ayıklama sürecini hızlandırır, 
# * kod kalitesini artırır ve gelecekteki değişikliklerin mevcut işlevselliği etkilemediğini doğrulamak için 
# * güven verir.

# ? pycache
# * __pycache__, Python tarafından oluşturulan derlenmiş bytecode dosyalarının (.pyc uzantılı) saklandığı 
# * bir klasördür. Python, Python kaynak kodunu çalıştırmadan önce bu kaynak kodunu derler ve 
# * bir bytecode oluşturur. Bu derlenmiş bytecode dosyaları, kaynak kodun çalıştırılması sırasında 
# * Python yorumlayıcısının daha hızlı çalışmasına yardımcı olur.
# * Python yorumlayıcısı, .pyc dosyalarını .py kaynak kodunu derlerken veya çalıştırırken oluşturur ve 
# * daha sonra bu derlenmiş bytecode dosyalarını, aynı kaynak kodunu daha hızlı bir şekilde 
# * yeniden yorumlamak için kullanır. Bu şekilde, Python kodu her çalıştırıldığında tekrar tekrar 
# * derlenme işlemi gerekmeyeceğinden, çalışma zamanında bir miktar performans artışı elde edilir.
# * __pycache__ klasörü, Python'un derlenmiş bytecode dosyalarını sakladığı yerdir. 
# * Proje dizininde bulunan Python modülleri her çalıştırıldığında veya ithal edildiğinde, 
# * bu klasörde .pyc dosyaları oluşturulur veya güncellenir. Klasör, Python sürümüne ve modülün bulunduğu 
# * konuma göre organize edilir.
# * __pycache__ klasörü, kaynak kodunu değiştirdiğinizde veya Python'u güncellediğinizde 
# * otomatik olarak yönetilir. Python, değiştirilmiş veya güncellenmiş kaynak kodlarını otomatik olarak 
# * yeniden derleyerek güncellenmiş .pyc dosyalarını oluşturur. 
# * Bu nedenle genellikle bu klasörle manuel olarak etkileşime gerek yoktur.


