
# ! REGISTER

# ? 1. register.html
# * MDBootstrap üzerinden register sayfamızı oluşturalım.
# * Öncelikle yine html iskeletimizi oluşturup main block kısmına;
# <div class="container py-5 h-100">
#     <div class="row d-flex justify-content-center align-items-center h-100">
#       <div class="col-xl-10">
#         <div class="card rounded-3 text-black">
#           <div class="row g-0 d-flex justify-content-center">
#             <div class="col-lg-6 gradient-custom">
#               <div class="card-body p-md-5 mx-md-4">
#                 <form method="POST">
#                   {% csrf_token %}
#                   <div class="form-outline mb-4">
#                     <input name="username" type="text" id="form2Example11" class="form-control" />
#                     <label class="form-label" for="form2Example11">Kullanıcı Adı</label>
#                   </div>
#                   <!-- Email input -->
#                   <div class="form-outline mb-4">
#                     <input name="email" type="email" id="form3Example3" class="form-control" />
#                     <label class="form-label" for="form3Example3">Email</label>
#                   </div>
#                   <!-- Password input -->
#                   <div class="form-outline mb-4">
#                     <input name="password1" type="password" id="form3Example4" class="form-control" />
#                     <label class="form-label" for="form3Example4">Şifre</label>
#                   </div>
#                   <div class="form-outline mb-4">
#                     <input name="password2" type="password" id="form3Example4" class="form-control" />
#                     <label class="form-label" for="form3Example4">Şifre Tekrar:</label>
#                   </div>
#                   <!-- Submit button -->
#                   <button type="submit" class="btn btn-primary btn-block mb-4">
#                     Kayıt Ol
#                   </button>
#                   <!-- Register buttons -->
#                   <div class="text-center">
#                     <p>Hesabınla Giriş Yap :</p>
#                     <button type="button" class="btn btn-link btn-floating mx-1">
#                       <i class="fab fa-facebook-f"></i>
#                     </button>
#                     <button type="button" class="btn btn-link btn-floating mx-1">
#                       <i class="fab fa-google"></i>
#                     </button>
#                     <button type="button" class="btn btn-link btn-floating mx-1">
#                       <i class="fab fa-twitter"></i>
#                     </button>
#                     <button type="button" class="btn btn-link btn-floating mx-1">
#                       <i class="fab fa-github"></i>
#                     </button>
#                   </div>
#                 </form>
#               </div>
#             </div>
#             </div>
#           </div>
#         </div>
#       </div>
#     </div>
#   </div>
# * login ile çok benzer bir register sayfası oluşturuyoruz.

# ? 2. models.py
# * user app'i içindeki modelse gelip kullanıcı bilgisi için bir userinfo modeli oluşturacağız.
# * ilk önce user importunu yapıyoruz;
# from django.contrib.auth.models import User
# * Ardından modelimizi oluşturalım;
# class UserInfo(models.Model):
#    user = models.OneToOneField(User,verbose_name=("Kulanıcı"), on_delete=models.CASCADE)#* user modeline bağlıyoruz
#    password = models.CharField(("Şifre"), max_length=50,null=True, blank=True)
# 
#    class Meta:
#       verbose_name_plural = 'Kullanıcı Bilgileri'   
# 
#    def __str__(self):  
#       return self.user.username
# * migration işlemlerimizi yapıp modeli veritabanına tanıtıp kaydedelim.

# ? 3. views.py
# * register fonksiyonumuzu oluşturup fonksiyon içeriğini yazalım;
# def registerPage(request):
# 
#     if request.method == "POST": #* form methodu POST ise bilgileri eşleştiriyoruz
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")
# 
#         if password1 == password2: #* eğer girilen şifreler eşleşiyorsa
#             if not User.objects.filter(username=username).exists(): #* Kullanıcı adı mevcut değil ise
#                 if not User.objects.filter(email=email).exists(): #* email adresi mevcut değil ise
#                     user = User.objects.create_user(
#                         username=username, email=email, password=password1)#* bilgileri alarak yeni bir kullanıcı oluştur
# 
#                     userinfo = UserInfo(user=user) #* userinfo modeline atama yapıyoruz
#                     userinfo.save() #* kullanıcıyı kaydettik
#                     messages.success(
#                         request, 'Kaydınız başarıyla oluşturuldu..') #* kayıt başarılı mesajı
#                     return redirect("login")
#                 else:
#                     messages.warning(request, 'Bu mail zaten kullanılıyor!!') #* hata mesajı
#                     return redirect("login") #* login sayfasına yönlendirme
#             else:
#                 messages.warning(
#                     request, 'Bu kullanıcı adı daha önceden alınmış!!') #* hata mesajı
#                 return redirect("login") #* login sayfasına yönlendirme
#         else: #* şifreler uyuşmuyorsa
#             messages.warning(request, 'Şifreler aynı değil!!') #* hata mesajı
#             return redirect("register") #* register sayfasına yönlendirme
# 
#     context = {}
# 
#     if request.user.is_authenticated: #* Eğer kullanıcı girişli ise;
#         return redirect("index") #* anasayfaya yönlendirme
#     return render(request, 'register.html', context)


# ? 4. urls.py
# * Register sayfasının path'ini yazıyoruz
#      path('register/',registerPage, name='register'),

# ? 5. login sayfası linkleme
# * login sayfasından register sayfasına yönlendirme için hesap oluştur bölümümüze linkleme yapıyoruz
# * {% url 'register' %}

# ? 6. Kullanıcı oluşturma
# * Register sayfamızdan bir kullanıcı oluşturup onunla login işlemlerini deneyelim.

# ! Tebrikler! Artık Kullanıcı oluşturabiliyoruz!
