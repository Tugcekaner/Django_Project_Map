
# ! ÜRÜNLER

# ? 1. model oluşturma
# * market/models.py içine importlarımızı yapıyoruz;
# * from django.contrib.auth.models import User
# * from django.utils.text import slugify

# ? 2. Kategori modeli
# * Ürünler için öncelikle kategori oluşturuyoruz.
# class Category(models.Model):
#     title = models.CharField(("Kategori"), max_length=50) #* kategori adı
#     slug = models.SlugField(("Slug"), blank=True) #* kategori slug oluşturma
# 
#     def save(self, *args, **kwargs): #* kategori için slug oluşturup kaydeden fonksiyon
#         self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
# 
#     class Meta: #* admin panelde görüntülenecek isimlendirme
#         verbose_name_plural = 'Kategoriler' #* çoğul kısım için
#         verbose_name = 'Kategori'  #* tekil kısım için
# 
#     def __str__(self): #* class için görünecek bilgi
#         return self.title

# ! notlar:
# * max_length=50 => max kullanılabilecek karakter sayısı
# * blank=True => boş bırakılabilmeyi sağlar, hata vermez.


# ? 3. Ürün modeli
#class Product(models.Model):
#    user = models.ForeignKey(User, verbose_name=(
#        "Kullanıcı - Satıcı"), on_delete=models.CASCADE) #* ürünü ekleyen usera bağlama
#    category = models.ForeignKey(Category, verbose_name=(
#        "Kategori"), on_delete=models.CASCADE,null=True) #* kategoriye bağlama
#    title = models.CharField(("Ürün adı"), max_length=50)
#    text = models.TextField(("İçerik")) #* ürün açıklaması
#    image = models.FileField(
#        ("Ürün Resmi"), upload_to='product', max_length=100) #* ürün görseli
#    date_now = models.DateField(("Tarih"), auto_now_add=True) #* eklendiği tarih
#    stok = models.IntegerField(("Stok")) #* stok sayısı
#    price = models.FloatField(("Fiyat"), blank=True, null=True) #* ürün fiyatı
#
#    def __str__(self):  #* class için görünecek bilgi
#        return self.title
#    
#    class Meta:  #* admin panelde görüntülenecek isimlendirme
#        verbose_name_plural = 'Ürünler'
#        verbose_name = 'Ürün'

# ! notlar:
# * verbose_name => field isimlendirmesi için
# * on_delete=models.CASCADE => silinme durumu için, CASCADE ile bağlı olan tüm classların silinmesini sağlar
# * null=True => sonradan eklenen bir model özelliğinde kullanılır, ekli modele ait kısım boşsa hata vermemesi için
# * upload_to='product' => ürün resminin nereye kaydedileceğini, yolunu belirtir.
# * auto_now_add=True => otomatik olarak o anın tarihini ekler.

# ? 4. admin panelde modelleri görüntüleyebilme
# * market/admin.py dosyasına öncelikle models dosyasını import ediyoruz.
# * from .models import *
# * Ardından görüntülenecek modelleri ekliyoruz;
#  admin.site.register(Category)
#  admin.site.register(Product)

# ? 5. migrateleri yapma
# * Oluşturulan modelleri veritabanına ekleyip güncellemeliyiz.
# * Bunun için öncelikle terminalde ctrl+c ile serverı kapatıyoruz.
# * Sırasıyla aşağıdaki komutları giriyoruz;
# * py manage.py makemigrations - değişiklikleri işliyoruz
# * py manage.py migrate - veritabanına kaydediyoruz
# * py manage.py runserver - projeyi çalıştırıyoruz

# ? 6. kategori-ürün ekleme
# * admin panele daha önce oluşturduğumuz admin ad ve şifresiyle giriş yapıyoruz.
# * Önce 5 adet kategori ekleyelim. Slug alanını boş bırakmayı unutmayalım, otomatik dolduracak.
# * Kategorileri eklediğimize göre şimdi de 10 adet ürün ekleyelim.

# ? 7. Admin panel görünüm ayarlama
# * Admin panelde eklenen ürün/kategorilerin hangi bilgilerinin görünmesini istiyorsak onları ayarlayalım.
# * market/admin.py içine;
#class CategoryView(admin.ModelAdmin):
#    list_display = ['title','slug']
#class ProductView(admin.ModelAdmin):
#    list_display = ['title','category','stok','price']
#    list_filter = ['category','price']
# * ardından bu yeni classları admin.py'a eklediğimiz modellere tanımlıyoruz.
# admin.site.register(Category,CategoryView)
# admin.site.register(Product,ProductView)

# ! notlar:
# * list_display => görüntülenecek bilgi
# * list_filter => panelde filtreleme imkanı

# ? 8. index sayfasında ürünleri görüntüleme - views.py
# * views.py içinde index fonksiyonumuzu açıyoruz.
# * Oluşturduğumuz kategori ve ürün modellerini fonksiyon içerisine alıyoruz.
#    kategoriler = Category.objects.all()
#    urunler = Product.objects.all()
# * ardından sayfada görüntülemek istediğimiz veriler için bir context oluşturup içeriğini dolduruyoruz;
#    context = {
#        'kategoriler': kategoriler,
#        'urunler': urunler
#    }
# * sayfada kategoriler ve urunler isimleriyle verileri çekebileceğiz.
# * render alanına da en sona context parametresini ekliyoruz;
#  return render(request,'index.html',context)

# ? 9. index.html içine verileri çekme
# * views.py içinde tanımladığımız verileri kullanacağız.
# * index.html içinde block main kısmına geliyoruz.
# * MdBootstrap'ten bir card yapısı alalım;
#<div class="card" style="width: 18rem;">
#  <img src="https://mdbcdn.b-cdn.net/img/new/standard/city/062.webp" class="card-img-top" alt="Chicago Skyscrapers"/>
#  <div class="card-body">
#    <h5 class="card-title">Card title</h5>
#    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
#  </div>
#  <ul class="list-group list-group-light list-group-small">
#    <li class="list-group-item px-4">Cras justo odio</li>
#    <li class="list-group-item px-4">Dapibus ac facilisis in</li>
#    <li class="list-group-item px-4">Vestibulum at eros</li>
#  </ul>
#  <div class="card-body">
#    <a href="#" class="card-link">Card link</a>
#    <a href="#" class="card-link">Another link</a>
#  </div>
#</div>
# * Burada ufak değişiklikler yaparak ürünlerimizin tamamını anasayfada görüntüleyeceğiz.
# * Block main içine öncelikle bir container ve row açıyoruz.
# * Tüm ürünleri görüntüleyebilmek için for döngüsüne ihtiyacımız var.
# * {% for urun in urunler %} diyerek tüm ürünleri döngüye alıyoruz.
# * döngünün içine card yapımızı yapıştırıyoruz.
# * Ardından kartı dinamik hale getirebilmek için tag içlerinde döngüde urun nesnesinin özelliklerine ulaşacağız.
# * Örneğin ürünün adını almak için {{ urun.title }} 
# * Bir block kart yapısı örneği;
# {% block main %}
# <div class="container">
#     <div class="row d-flex justify-content-between">
#         {% for urun in urunler %} #* for başlangıcı
#         <div class="col-md-4 col-12 my-3">
#             <div class="card" style="width: 18rem;">
#                 <img src="{{ urun.image.url }}" class="card-img-top" #* ürün resmi
#                     alt="Chicago Skyscrapers" />
#                 <div class="card-body">
#                     <h5 class="card-title">{{ urun.title }}</h5> #* ürün adı
#                     <p class="card-text">{{ urun.text|truncatechars:20 }}</p> #* ürün açıklaması
#                 </div>
#                 <ul class="list-group list-group-light list-group-small">
#                     <li class="list-group-item px-4">Tarih : {{ urun.date_now }}</li> #* ürün tarihi
#                     <li class="list-group-item px-4">Stok : {{ urun.stok }}</li> #* stok sayısı
#                     <li class="list-group-item px-4">Fiyat : {{ urun.price }} tl</li> #* fiyatı
#                 </ul>
#                 <div class="card-body">
#                     <a href="#" class="btn btn-warning">Ürün Detayı</a> #* sonra detay sayfasına gideceğiz
#                     <a href="#" class="btn btn-info">Satın Al</a> #* sonra sepete ekleme işlemi yaptırılacak
#                 </div>
#             </div>
#         </div>
#         {% endfor %} #* for bitişi
#     </div>
# </div>
# {% endblock main %}

# ! notlar:
# * truncatechars => uzun yazıda kaç karakter görünmesini istiyorsak o parametreyi veriyoruz.

# ! Tebrikler! Artık ürünlerimiz anasayfada görüntülenebiliyor!
