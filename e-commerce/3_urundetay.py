
# ! ÜRÜN DETAY SAYFASI

# ? 1. Detay sayfa oluşturma
# * market/templates içine detail.html adında bir dosya açıyoruz.
# * extendleri yapıp iskeleti oluşturuyoruz.
# {% extends 'base.html' %}
# {% load static %}
# {% block title %}
# <title>Ürün Detay</title> #* title adını sayfaya göre güncelledik.
# {% endblock title %}
# {% block style %}
# {% endblock style %}
# {% block main %}
# {% endblock main %}

# ? 2. views - urls
# * views dosyamıza sayfayı görüntüleyebilmek için gerekli olan fonksiyonu giriyoruz.
# def detailPage(request):
#    return render(request,'detail.html')
# * urls içine detay sayfasının pathini ekliyoruz.
#    path('detail',detailPage,name='detail'),
# * http://127.0.0.1:8000/detail/ üzerinden sayfayı görüntüleyebiliyoruz.

# ? 3. card
# * Ürün detayı için MDBootstraptan card yapısı alıp yapıştırıyoruz. Değişiklikler yapacağız.
# <div class="container">
#     <div class="row d-flex justify-content-center my-5">
#         <div class="col-md-6 col-10">
#             <div class="card mb-3" style="max-width: 540px;">
#                 <div class="row g-0">
#                   <div class="col-md-4">
#                     <img
#                       src="https://mdbcdn.b-cdn.net/wp-content/uploads/2020/06/vertical.webp"
#                       alt="Trendy Pants and Shoes"
#                       class="img-fluid rounded-start"
#                     />
#                   </div>
#                   <div class="col-md-8">
#                     <div class="card-body">
#                       <h5 class="card-title">Card title</h5>
#                       <p class="card-text">
#                         This is a wider card with supporting text below as a natural lead-in to
#                         additional content. This content is a little bit longer.
#                       </p>
#                       <p class="card-text">
#                         <small class="text-muted">Last updated 3 mins ago</small>
#                       </p>
#                     </div>
#                   </div>
#                 </div>
#               </div>
#         </div>
#     </div>
# </div>
# * ürünlere idleri üzerinden ulaşarak detaylarına erişeceğiz.

# ? 4. views.py
# * views.py dosyasına geri dönüp öncelikle import gerçekleştireceğiz.
# * from django.shortcuts import render,redirect,get_object_or_404
# * sadece render olan importa get_object_or_404 ve redirect eklemesi yapıyoruz.
# * Bu sayede ürün  bulunamazsa kullanıcı 404 hatası alacak.
# * Ardından detailPage fonksiyonunu güncelliyoruz;
#def detailPage(request,id): #* id parametresini ekledik
#    product = get_object_or_404(Product,id=id) #* idsine göre ürünü çekmemize yarayan kod
#    context={
#        'product': product,
#    }
#    return render(request,'detail.html',context)
# * Artık elimizde ürün idsine göre yönlendirme yapabileceğimiz bir view fonksiyonumuz mevcut.

# ? 5. urls.py
# * DetailPage pathini güncelliyoruz;
#     path('detail/<id>',detailPage,name='detail'),
# * eklediğimiz <id> ile ürün idsine ait detay sayfasına ulaşacağız.

# ? 6. indexte linkleme
# * indexte ürün card yapımızda bulunan ürün detayına gitme kısmına geliyoruz.
# * a tagi içerisindeki yönlendirmeyi güncelliyoruz;
# href="/detail/{{ urun.id }}"
# * bu yönlendirme bilgileri alınan ürünün id'sine ulaşıp o ürünün detay sayfasına gitmemizi sağlıyor.

# ? 7. detay sayfa ürün bilgilerini getirme
# * views dosyasında product üzerinden aldığımız bilgileri sayfaya yansıtacağız.
# * tek bir ürün olduğu için direkt {{ product.title }} vb. diyerek ulaşabiliyoruz.
# * güncellemeleri yaptıktan sonra card yapımız aşağıdaki gibi olmalı;
# <div class="container">
#     <div class="row d-flex justify-content-center my-5">
#         <div class="col-md-9 col-10">
#             <div class="card mb-3" style="max-width: 6000px;">
#                 <div class="row g-0">
#                   <div class="col-md-4 d-flex">
#                     <img
#                       src="{{ product.image.url }}"
#                       alt="Trendy Pants and Shoes"
#                       class="img-fluid align-self-center"
#                     />
#                   </div>
#                   <div class="col-md-8">
#                     <div class="card-body">
#                       <h5 class="card-title">{{ product.title }}</h5>
#                       <hr>
#                       <p class="card-text">
#                         {{ product.text }}
#                       </p>
#                       <hr>
#                       <p class="card-text">
#                         <small class="text-muted">Eklenme tarihi : {{ product.date_now }}</small><br>
#                         <small class="text-muted">Stok sayısı : {{ product.stok }}</small><br>
#                         <small class="text-muted">Fiyat : {{ product.price }} TL</small>
#                       </p>
#                       <a href="#" class="btn btn-info">Satın Al</a>
#                     </div>
#                   </div>
#                 </div>
#               </div>
#         </div>
#     </div>
# </div>
# * product modelinde yer alan istenilen tüm bilgileri görüntüleyebiliriz.

# ! Tebrikler! Ürün detay sayfanız hazır!

