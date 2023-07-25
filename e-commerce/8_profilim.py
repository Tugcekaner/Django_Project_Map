
# ! PROFİLİM SAYFASI

# ? 1. html
# * user/templates içerisine profile.html dosyası açıyoruz.
# * Burada girişli olan kullanıcının profil bilgilerini görebilme, profil bilgilerini
# * ve şifresini güncelleyebilme işlemleri olacak.
# * Hem bilgi gösterip hem de bilgi alacağımız için form kullanmalıyız.
# * İstediğiniz şekilde bir önyüz ayarlayabilirsiniz, bir örnek de yine vereceğiz.

# ? 2. js
# * Güzel bir görünüm elde edebilmek adına 2 card yapısını aynı sayfada kullanacağız.
# * Bunun için javascripte ihtiyacımız var.
# * base.html içerisine body kapanışının hemen üstüne bir block yapısı açıp js adını veriyoruz.
# {% block js %}

# ? 3. profile.html içeriği
# * Örnek önyüz için kodlarımız aşağıdaki gibi olmalı;
# {% extends 'base.html' %}
# {% block style %}
# <style>#* js display none-block kullanabilmek için
#     #card2 { 
#        display: none;
#     }
#  </style>
# {% endblock style %}
# {% block main %}
# <div class="container">
#     <div class="row d-flex justify-content-center align-items-center h-100">
#         <div class="col col-lg-10 mb-4 mb-lg-0">
#             <!-- card1 start -->
#             <div class="card my-4" id="card1" style="border-radius: .5rem;">
#                 <div class="row g-0">
#                     <div class="col-md-4 text-center bg-light"
#                         style="border-top-left-radius: .5rem; border-bottom-left-radius: .5rem;">
#                         <img src="https://blog-frontend.envato.com/cdn-cgi/image/width=1200,quality=75,format=auto/uploads/2022/04/E-commerce-App-JPG-File-scaled.jpg" alt="Avatar" 
#                         class="img-fluid my-5" style="width: 80px; border-radius: 50%; height: 80px; object-fit: cover;" />
#                         <h5>Kullanıcı Adı :</h5>
#                         <h5>{{ user.username }}</h5>
#                         <i class="far fa-edit mb-5" onclick="changeProfil()"></i>
#                     </div>
#                     <div class="col-md-8">
#                         <div class="card-body p-4">
#                             <h6 class="text-danger">Bilgiler</h6>
#                             <hr class="mt-0 mb-4">
#                             <div class="row pt-1">
#                                 <div class="col-6 mb-3">
#                                     <h6>İsim :</h6>
#                                     <p class="text-dark">{{ user.first_name }}</p>
#                                 </div>
#                                 <div class="col-6 mb-3">
#                                     <h6>Soyisim :</h6>
#                                     <p class="text-dark">{{ user.last_name }}</p>
#                                 </div>
#                             </div>
#                             <div class="row pt-1">
#                                 <div class="col-6 mb-3">
#                                     <h6>E-mail :</h6>
#                                     <p class="text-dark">{{ user.email }}</p>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <!-- CARD 2 START -->
#             <div class="card mb-3 h-100 my-4" id="card2" style="border-radius: .5rem;">
#                 <form class="row g-0 h-100" method="POST" enctype="multipart/form-data">
#                     {% csrf_token %}
#                     <div class="col-md-4 gradient-custom text-center text-white bg-dark"
#                         style="border-top-left-radius: .5rem; border-bottom-left-radius: .5rem;">
#                         <img src="https://blog-frontend.envato.com/cdn-cgi/image/width=1200,quality=75,format=auto/uploads/2022/04/E-commerce-App-JPG-File-scaled.jpg" alt="Avatar" class="img-fluid my-5"
#                             style="width: 80px; border-radius: 50%; height: 80px; object-fit: cover;" />
#                         <br>
#                         <hr>
#                         <div class="d-flex justify-content-between align-items-center px-3 my-1">
#                             <h6>İsim :</h6>
#                             <input name="name" class="form-control d-inline-flex" style="width: 200px;" type="text"
#                                 value="{{ request.user.first_name }}">
#                         </div>
#                         <div class="d-flex justify-content-between align-items-center px-3 my-1">
#                             <h6>Soy isim :</h6>
#                             <input name="surname" class="form-control d-inline-flex" style="width: 200px;" type="text"
#                                 value="{{ request.user.last_name }}">
#                         </div>
#                         <div class="d-flex justify-content-between align-items-center px-3 my-1">
#                             <h6>Kullanıcı :</h6>
#                             <input name="username" class="form-control d-inline-flex" style="width: 200px;" type="text"
#                                 value="{{ request.user }}">
#                         </div>
#                         <i class="far fa-edit mb-3" onclick="changeProfil()"></i><br>
#                         <button type="submit" class="btn btn-success mb-2" name="submit"
#                             value="profileUpdate">Kaydet</button>
#                     </div>
#                     <div class="col-md-8">
#                         <div class="card-body p-4">
#                             <h6 class="text-danger" >Bilgiler</h6>
#                             <hr class="mt-0 mb-4">
#                             <div class="row pt-1">
#                                 <div class="col-6 mb-3">
#                                     <h6>E-mail</h6>
#                                     <input name="email" class="form-control d-inline-flex" style="width: 200px;"
#                                         type="text" value="{{ request.user.email }}">
#                                 </div>
#                                 <div class="col-6 mb-3">
#                                     <h6>Şifre</h6>
#                                     <!-- Button trigger modal -->
#                                     <button type="button" class="btn btn-primary" data-mdb-toggle="modal"
#                                         data-mdb-target="#exampleModal">
#                                         Şifre Değiştir
#                                     </button>
#                                     <!-- Modal -->
#                                     <div class="modal fade" id="exampleModal" tabindex="-1"
#                                         aria-labelledby="exampleModalLabel" aria-hidden="true">
#                                         <div class="modal-dialog">
#                                             <div class="modal-content">
#                                                 <div class="modal-header">
#                                                     <h5 class="modal-title" id="exampleModalLabel">Şifre Değiştir</h5>
#                                                     <button type="button" class="btn-close" data-mdb-dismiss="modal"
#                                                         aria-label="Close"></button>
#                                                 </div>
#                                                 <div class="modal-body">
#                                                     <div
#                                                         class="d-flex justify-content-between align-items-center px-3 my-1">
#                                                         <h6>Eski Şifre:</h6>
#                                                         <input name="password" class="form-control d-inline-flex"
#                                                             style="width: 200px;" type="password">
#                                                     </div>
#                                                     <div
#                                                         class="d-flex justify-content-between align-items-center px-3 my-1">
#                                                         <h6>Yeni Şifre:</h6>
#                                                         <input name="password1" class="form-control d-inline-flex"
#                                                             style="width: 200px;" type="password">
#                                                     </div>
#                                                     <div
#                                                         class="d-flex justify-content-between align-items-center px-3 my-1">
#                                                         <h6>Tekrar Yeni Şifre:</h6>
#                                                         <input name="password2" class="form-control d-inline-flex"
#                                                             style="width: 200px;" type="password">
#                                                     </div>
#                                                 </div>
#                                                 <div class="modal-footer">
#                                                     <button type="submit" name="submit" value="passwordChange"
#                                                         class="btn btn-primary">Şifreyi Değiştir</button>
#                                                     <button type="button" class="btn btn-secondary"
#                                                         data-mdb-dismiss="modal">Vazgeç</button>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                     </div>
#                                     <!-- modal end -->
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                 </form>
#             </div>
# 
#         </div>
#     </div>
# </div>
# {% endblock main %}
# {% block js %}
# <script>
#     changecard = true;
#     var changeProfil = () => {
#         if (changecard) {
#             document.getElementById("card1").style.display = "none";
#             document.getElementById("card2").style.display = "block";
#         } else {
#             document.getElementById("card1").style.display = "block";
#             document.getElementById("card2").style.display = "none";
#         }
#         changecard = !changecard
#     }
# </script>
# {% endblock js %}
# * Kodları inceleyerek nerelerde bilgi alındığını, nerelerde bilgi gösterildiğini muhakkak görelim.

# ? 4. views
# * user/views.py içerisine sayfamızın fonksiyonunu yazalım
#def profilePage(request):
#    profile = UserInfo.objects.filter(user=request.user) #* profil için kullanıcı bilgileri modelini eşleştiriyouz
#    user = User.objects.get(username=request.user) #* girişli kullanıcıyı alıyoruz
#* birden fazla sumbit olduğu için iflerle ayıracağız
#    if request.method == "POST": #* Eğer form metodu POST ise; 
#        submit = request.POST.get("submit") 
#        if submit == "profileUpdate": #* eğer submit profili güncelle/kaydet butonuysa
#            fname = request.POST.get("name") #* posttan gelen bilgileri isimlendiriyoruz
#            lname = request.POST.get("surname")
#            email = request.POST.get("email")
#            username = request.POST.get("username")
#
#            user.first_name = fname #* posttan gelen isimlendirdiğimiz bilgilerin user için karşılıkları
#            user.last_name = lname
#            user.email = email
#            
#            if not User.objects.filter(username=username).exists(): #* eğer kullanıcı adı daha öcne alınmamış ise;
#                user.username = username
#                messages.success(
#                    request, "Kullanıcı adınız başarıyla değiştirildi..")
#            else:
#                messages.warning(
#                    request, "Bu kullanıcı adı zaten kullanılıyor!")
#        if submit == "passwordChange": #* eğer submit şifre değiştirme ise
#            password = request.POST.get("password")
#            if user.check_password(password):  #* şifre kontrolü
#                password1 = request.POST.get("password1")
#                password2 = request.POST.get("password2")
#                if password1 == password2:
#                    user.set_password(password1)  #* şifre değiştirme
#                    profile.password = password1 #* yeni şifreyi atama
#                    login(request, user) #* kullanıcıya tekrar giriş yaptırma
#                    messages.success(
#                        request, "Şifreniz başarıyla değiştirildi..")
#                else:
#                    messages.warning(request, "Şifreler eşleşmiyor!")
#            else:
#                messages.warning(request, "Şifreniz yanlış!")
#
#            profile.save() #* profili kaydetme
#        user.save() #* kullanıcıyı kaydetme
#        return redirect('profile')
#
#    context = {
#        "profile": profile,
#        "user": user,
#    }
#
#    return render(request, 'profile.html', context)
# * Fonksiyonları yazarken özellikle uzun fonksiyonlarda tablara çok dikkat edilmeli!

# ? 5. urls
# * urls.py dosyamıza sayfamızı eklememiz gerekli.
# * user bölümüne;
#     path('profile/',profilePage,name='profile'),
# * olarak eklememizi yapıyoruz. 

# ? 6. navbar link
# * Kullanıcı kısmında dropdown bölümüne linke eklemesi yapacağız.
# * {% url 'profile' %} yönlendirmesini de yaparak tıklandığında profil sayfasına erişiyoruz.

# ! Tebrikler! Artık profil güncellemesi, şifre değişiklikleri de yapabiliyor ve bunları veritabanında saklayabiliyorsunuz!

