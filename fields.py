
# ! FIELDS
 
# ? CharField:
# * Metin tabanlı alanı temsil eder. Örneğin, kullanıcı adı veya başlık gibi kısa metinler için kullanılır.
 
# ? TextField: 
# * Uzun metin tabanlı alanı temsil eder. Blog içerikleri gibi daha uzun metinler için kullanılır.
 
# ? IntegerField: 
# * Tam sayı değeri için alanı temsil eder. Örneğin, bir ürünün stok adeti gibi tamsayı değerleri için kullanılır.
 
# ? FloatField: 
# * Ondalık noktalı sayıları temsil eder. Örneğin, bir ürünün fiyatı gibi ondalık sayılar için kullanılır.
 
# ? DateField: 
# * Tarih değerlerini temsil eder. Örneğin, bir etkinliğin tarihi gibi tarihler için kullanılır.
 
# ? TimeField: 
# * Saat değerlerini temsil eder. Örneğin, bir etkinliğin başlama saati gibi saatler için kullanılır.
 
# ? DateTimeField: 
# * Tarih ve saat değerlerini bir arada temsil eder. Örneğin, bir blog yazısının yayınlanma 
# * tarihi ve saati için kullanılır.
 
# ? BooleanField: 
# * Mantıksal (doğru/yanlış) değerleri temsil eder. Örneğin, bir ürünün stokta olup olmadığını 
# * belirlemek için kullanılır.
 
# ? ForeignKey: 
# * Bir diğer model ile ilişki kurar. Bir modeldeki bir alanın başka bir modelin anahtarını 
# * (primary key) göstermesini sağlar. İlişkisel veritabanı yapıları oluşturmak için kullanılır.
 
# ? ManyToManyField: 
# * Birden fazla modeli ilişkilendiren çok-noktalar arası (many-to-many) ilişkileri temsil eder. 
# * Örneğin, bir etkinlikte birden çok konuşmacı ve bir konuşmacının birden çok etkinlikte yer alması gibi senaryolarda kullanılır.
 
# ? EmailField: 
# * Geçerli bir e-posta adresini temsil eder. E-posta adreslerini tutmak için kullanılır.
 
# ? ImageField: 
# * Resim dosyalarını temsil eder. Kullanıcılara resim yükleme imkanı vermek için kullanılır.
 
# ? FileField: 
# * Herhangi bir dosya türünü temsil eder. Kullanıcılara dosya yükleme imkanı vermek için kullanılır.
 
# ? URLField: 
# * Geçerli bir web adresini (URL) temsil eder. Web adreslerini tutmak için kullanılır.
 
# ? SlugField: 
# * URL uyumlu "slug" değerlerini temsil eder. URL'lerde kullanılacak metinleri depolamak için kullanılır.
 
# ? DecimalField: 
# * Ondalıklı sayıları temsil eder. Hassas ondalık sayıları gerektiren finansal veriler için kullanılır.
 
# ? DurationField: 
# * Zaman dilimini (saniye ve mikrosaniye) temsil eder. Süreleri depolamak için kullanılır.
 
# ? BinaryField: 
# * İkili (binary) veri türünü temsil eder. Örneğin, dosya içeriğini depolamak için kullanılabilir.
 
# ? IPAddressField: 
# * IP adreslerini temsil eder. IP adreslerini depolamak için kullanılır.
 
 
