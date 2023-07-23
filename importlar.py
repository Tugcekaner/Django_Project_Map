
# ! IMPORTLAR

# ? import os
# * Django'da "os" (işletim sistemi) modülü, Python programlarının işletim sistemleriyle 
# * etkileşime girmesine ve çeşitli işletim sistemi bağımlı işlevleri gerçekleştirmesine 
# * yardımcı olan bir modüldür. Bu modül, özellikle Django gibi web çerçevelerinde, 
# * dosya yollarını oluşturmak, dosyaları yönetmek, ortam değişkenlerine erişmek ve 
# * diğer işletim sistemi işlevlerini gerçekleştirmek için kullanılır.

# ? from django.conf.urls.static import static
# * from django.conf.urls.static import static, Django projelerinde static dosyalarını 
# * geliştirme ortamında (DEBUG modunda) servis etmek için kullanılan bir yardımcı 
# * fonksiyondur. Django, geliştirme ortamında static dosyalarını (örneğin, CSS, JavaScript, resimler) 
# * otomatik olarak servis etmez. Ancak, static() fonksiyonuyla bu dosyaları servis etmek kolaylaşır.
# * static() fonksiyonu, static dosyalarını belirtilen URL kökünden (STATIC_URL) çözümlemek için kullanılır. 
# * Ayrıca, belirtilen dosya sistemi yolu (STATIC_ROOT) altındaki static dosyalarını bulur ve 
# * HTTP isteklerine yanıt olarak bu dosyaları geri gönderir.
# * static() fonksiyonunun kullanımı genellikle urls.py dosyasında proje URL yapılandırmasını yaparken yapılır.

# ? from django.conf import settings
# * from django.conf import settings, Django projelerinde settings.py dosyasında tanımlanan ayarları 
# * kullanmak için kullanılan bir Python modülüdür. settings.py dosyası, Django projelerinin 
# * yapılandırma ayarlarını içeren dosyadır ve projenin davranışını kontrol etmek için kullanılır.
# * settings.py dosyasında, projenin çeşitli ayarları belirtilir. Bu ayarlar, veritabanı bağlantıları, 
# * statik dosyaların konumu, şablonların konumu, dil ve zaman dilimi ayarları, güvenlik ayarları, 
# * oturum yönetimi ve daha birçok proje özelliği için yapılandırmaları içerir.
# * from django.conf import settings ifadesi, settings.py dosyasındaki ayarlara erişmek için kullanılır. 
# * Bu modül, projenin ayarlarını içeren bir sözlük olan settings nesnesine erişimi sağlar. 
# * settings.py dosyasında tanımlanan ayarlara, diğer Python dosyalarından bu şekilde erişebilir ve 
# * bu ayarları projenizde farklı yerlerde kullanabilirsiniz.

# ? from django.contrib.auth.models import User
# * Django'nun sağladığı kullanıcı kimlik doğrulama ve yetkilendirme sistemi için yerleşik User modelini 
# * projenize dahil etmek için kullanılır.
# * Django, kullanıcı kimlik doğrulama ve yetkilendirme işlemlerini kolaylaştırmak için User modeli gibi birçok 
# * önceden tanımlanmış model ve işlev içerir. Bu model, kullanıcıların kimlik bilgilerini ve yetkilendirme ile ilgili 
# * diğer özelliklerini depolar.
# * User modeli, Django'nun sağladığı django.contrib.auth uygulamasının bir parçasıdır. Bu uygulama, 
# * kullanıcı kimlik doğrulama, oturum yönetimi, gruplar ve izinler gibi kullanıcı yönetimi ile ilgili çeşitli işlevleri içerir. 
# * User modeli, kullanıcı adı, e-posta adresi, şifre gibi temel kullanıcı bilgilerini tutar ve kullanıcılar için kimlik doğrulama 
# * ve yetkilendirme işlemlerini yönetir.
# * Bu modeli projenize dahil ederek, Django'nun kullanıcı kimlik doğrulama sistemi üzerinden kullanıcıları oluşturabilir, 
# * güncelleyebilir, silebilir ve kimlik doğrulama işlemlerini gerçekleştirebilirsiniz. Örneğin, kullanıcıların kayıt olmasını, 
# * giriş yapmasını ve belirli sayfalara erişimini kontrol etmek için User modelini kullanabilirsiniz.

# ? from django.utils.text import slugify
# * Django'da metinleri URL dostu "slug" haline getirmek için kullanılan bir işlevi projenize dahil etmek için kullanılır.
# * URL "slug"ları, genellikle makale başlıkları, kategori adları veya herhangi bir metinle oluşturulan benzersiz ve 
# * insanlar tarafından okunabilir URL segmentleridir. Örneğin, "Python Django Nedir?" 
# * başlığının URL slug hali "python-django-nedir" şeklinde olabilir.
# * slugify() işlevi, alınan metni URL dostu bir slug haline dönüştürür. 
# * Metindeki boşlukları tire (-) ile değiştirir, büyük harfleri küçük harfe dönüştürür ve 
# * diğer özel karakterleri uygun şekilde işler. Bu şekilde, bir metni URL'de kullanılmak üzere 
# * uygun hale getirir ve olası URL uyumsuzluklarını önler.

# ? from django.shortcuts import get_object_or_404
# * get_object_or_404, Django web çerçevesindeki django.shortcuts modülünden bir fonksiyondur. 
# * Bu fonksiyon, veritabanından belirli bir model nesnesini almak için kullanılır. 
# * Eğer nesne bulunamazsa, HTTP 404 "Not Found" hatası döndürerek kullanıcıya uygun bir 
# * hata sayfası gösterilmesini sağlar.
# * Bu fonksiyon, özellikle Django projelerinde genellikle detay sayfalarında ve veritabanı nesnelerine 
# * erişimde sıklıkla kullanılır. Verilen model ve arama kriterleri ile nesneyi almaya çalışır ve 
# * nesneyi bulamazsa Django, varsayılan olarak "Page Not Found" (404) hatasını döndürür. 
# * Böylece kullanıcılar, kayıtlı olmayan bir öğeye erişmeye çalıştıklarında uygun bir hata sayfası görürler.

# ? from django.shortcuts import render
# * from django.shortcuts import render ifadesi, Django web çerçevesinde template tabanlı görüntüleme 
# * (view) fonksiyonlarını oluşturmak için kullanılan bir import ifadesidir. Bu ifade, Django'da 
# * bir kullanıcı isteğine yanıt olarak bir HTML şablonu içeriğini görüntülemek için kullanılan bir yöntemi çağırmayı sağlar.
# * render fonksiyonu, HTTP yanıtlarını oluşturmak için kullanılır ve genellikle Django projelerindeki 
# * view fonksiyonları içinde kullanılır. Bu fonksiyon, bir HTML şablonunu kullanıcıya göstermek için kullanılan 
# * Django projesinin "şablon motoru" ile entegre çalışır.

# ? from django.shortcuts import redirect
# * from django.shortcuts import redirect ifadesi, Django web çerçevesinde sayfa yönlendirmeleri yapmak için kullanılan 
# * bir import ifadesidir. Bu ifade, Django projesinde bir kullanıcı isteğine yanıt olarak, belirtilen URL'ye yönlendirme 
# * işlemlerini gerçekleştirmek için kullanılır.
# * redirect fonksiyonu, belirtilen URL'ye yönlendirmek için kullanılır. Bu, kullanıcının bir sayfada form gönderdikten sonra 
# * başka bir sayfaya yönlendirilmesi veya belirli bir sayfaya otomatik olarak yönlendirilmesi gereken durumlarda kullanışlıdır.

# ? import time
# * import time ifadesi, Python'daki standart kütüphaneden bir modül olan time modülünü içe aktarmak için kullanılır. 
# * Django ile doğrudan bir ilişkisi yoktur, ancak Python dilinde zamanla ilgili işlemleri yapmak için kullanılan önemli bir modüldür.
# * time modülü, zamanla ilgili işlevleri içerir ve çeşitli zaman işlemlerini gerçekleştirmek için kullanılır. 
# * Bu modülü içe aktardığınızda, zaman işlemleri için işlevler ve sabitler kullanılabilir.
# * Bazı yaygın kullanılan time modülü işlevleri şunlardır:
# ! time.time():Şu anki zamandan, 1970-01-01 00:00:00 UTC'den geçen saniye sayısını döndürür. 
# * Bu, Unix zamanı olarak da bilinir ve zaman damgası olarak adlandırılır.
# ! time.sleep(seconds):Belirtilen süre kadar (saniye cinsinden) işlemi duraklatır. 
# * Bu, belirli bir zaman gecikmesi eklemek veya işlemciyi belirli bir süre boyunca uyutmak için kullanılabilir.
# ! time.localtime():Şu anki yerel zamanı döndürür ve bunu bir zaman tuplesi şeklinde sunar 
# * (yıl, ay, gün, saat, dakika, saniye, haftanın günü, yılın günü, yaz saati uygulaması).
# ! time.strftime(format, time_tuple):Zaman tupelini belirtilen biçimlendirme şablonuna göre biçimlendirerek, 
# * insanlar tarafından okunabilir bir şekilde zaman dizesi oluşturur.
# ! time.gmtime():Şu anki zamanı UTC zamanı olarak döndürür.
# * Bu işlevler, zamanla ilgili işlemler yapmak istediğinizde veya belirli bir gecikme eklemek istediğinizde kullanışlı olabilir. 
# * Örneğin, bir işlemi belirli aralıklarla yürütmek, zaman damgası içeren verileri işlemek veya 
# * belirli bir süre beklemek için time modülünü kullanabilirsiniz.

# ? from django.contrib import messages
# * from django.contrib import messages ifadesi, Django'nun messages framework'ünü kullanmak için django.contrib.messages modülünü 
# * içe aktarır. Bu modül, web uygulamanızda kullanıcıya mesajlar göndermenize ve görüntülemenize olanak tanır. 
# * Kullanıcıya farklı durumlarda bilgi, uyarı, hata veya başarı mesajları göstermek için kullanılır.
# * messages framework'ü, HTTP isteklerinin birinden diğerine veri taşımak için kullanılan oturumlarla ilgilenir. 
# * Böylece, bir sayfada oluşturulan mesaj, kullanıcı diğer sayfaya geçtiğinde veya sayfayı yenilediğinde bile gösterilebilir.
# * Django'da messages framework'ü kullanırken, çeşitli mesaj türleri mevcuttur:
# * messages.info(request, message): Bilgi mesajı göstermek için kullanılır. 
# * Genellikle kullanıcıya bilgi vermek için kullanılır.
# * messages.success(request, message): Başarı mesajı göstermek için kullanılır. 
# * Kullanıcı, bir eylemi başarıyla tamamladığında veya olumlu bir geribildirim verildiğinde kullanılır.
# * messages.warning(request, message): Uyarı mesajı göstermek için kullanılır. 
# * Kullanıcıyı bir durum hakkında uyarmak veya dikkatini çekmek için kullanılır.
# * messages.error(request, message): Hata mesajı göstermek için kullanılır. 
# * Bir hata durumu veya beklenmeyen bir durumla karşılaşıldığında kullanıcıya bilgi vermek için kullanılır.
# * Bu mesaj türleri, kullanıcı deneyimini iyileştirmek ve kullanıcılara önemli bilgileri aktarmak için 
# * web uygulamanızda kullanışlıdır. Örneğin, bir kullanıcı hesap oluşturduğunda başarı mesajı gösterebilir, 
# * bir formu başarılı bir şekilde gönderdiğinde bilgi mesajı gösterebilir veya bir işlemde hata oluştuğunda hata mesajı gösterebilirsiniz.
# * Mesajları oluşturduktan sonra, bu mesajları şablon dosyalarınızda veya görüntüleme işlevlerinizde kullanarak 
# * kullanıcıya gösterebilirsiniz. Bu, kullanıcının geri bildirim alması ve etkileşimli bir deneyim yaşaması açısından önemlidir.

# ? from django.contrib.auth import login, logout, authenticate
# * from django.contrib.auth ifadesi, Django'da kullanıcı kimlik doğrulama ve yetkilendirme işlemleri için gerekli olan 
# * fonksiyonları ve sınıfları içeren auth (authentication) modülünü içe aktarır. Bu modül, web uygulamanızda kullanıcıları 
# * sisteme giriş yapmalarını, oturum açmalarını, çıkış yapmalarını ve kimlik doğrulama işlemlerini yönetmenize olanak tanır.
# * İşte içe aktarılan fonksiyonların ve sınıfların açıklamaları:
# * login(request, user): Bu fonksiyon, kullanıcı oturumunu başlatmak için kullanılır. 
# * Kullanıcı adı ve parola gibi kimlik bilgilerini doğruladıktan sonra authenticate() fonksiyonuyla kimlik doğrulama yapılır ve 
# * eğer kullanıcı bilgileri geçerliyse, login() fonksiyonu ile kullanıcı oturumu başlatılır. request parametresi, 
# * kullanıcının tarayıcısı ile sunucu arasında bilgi alışverişi sağlar. user parametresi ise kimlik doğrulaması başarılı olan 
# * kullanıcı nesnesini temsil eder.
# * logout(request): Bu fonksiyon, mevcut kullanıcının oturumunu sonlandırmak için kullanılır. 
# * Kullanıcı çıkış yapmak istediğinde logout() fonksiyonu çağrılır ve kullanıcının oturumu sonlandırılır.
# * authenticate(request, username=None, password=None): Bu fonksiyon, kullanıcının kimlik bilgilerini doğrulamak için kullanılır. 
# * Kullanıcı adı ve parola parametreleriyle çağrılır. Eğer kullanıcı adı ve parola doğruysa, kimlik doğrulaması 
# * başarılı bir şekilde gerçekleşir ve kimlik doğrulanmış kullanıcı nesnesi döndürülür. Doğrulama başarısız olursa None döner.
# * Bu fonksiyonlar, Django'da kullanıcı kimlik doğrulama ve oturum yönetimi işlemlerini kolaylaştırır. 
# * Web uygulamanızda kullanıcıları yetkilendirmek, sayfalara erişim kontrolü sağlamak ve kullanıcıların oturum açma ve 
# * çıkış yapma işlemlerini yönetmek için django.contrib.auth modülünden bu fonksiyonları kullanabilirsiniz. 
# * Bu sayede Django, güvenli ve kullanıcı dostu bir kimlik doğrulama süreci sunar.







