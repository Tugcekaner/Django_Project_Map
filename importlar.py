
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







