
# ! LOGIN SAYFASI - LOGIN İŞLEMLERİ

# ? 1. user/templates
# * user appi içinde templates klasörümüzü açıyoruz.
# * templates klasörüne login.html adında bir login sayfası oluşturuyoruz.

# ? 2. login.html
# * login.html içerisine extend ve blocklarla iskeletimizi oluşturuyoruz.
# * block main içerisine MDBootstrap'tan aldığımız basit bir login formu koyacağız.
# * Örn. aşağıdaki formu alalım;
# <form>
#   <!-- Email input -->
#   <div class="form-outline mb-4">
#     <input type="email" id="form2Example1" class="form-control" />
#     <label class="form-label" for="form2Example1">Email address</label>
#   </div>
#
#   <!-- Password input -->
#   <div class="form-outline mb-4">
#     <input type="password" id="form2Example2" class="form-control" />
#     <label class="form-label" for="form2Example2">Password</label>
#   </div>
#
#   <!-- 2 column grid layout for inline styling -->
#   <div class="row mb-4">
#     <div class="col d-flex justify-content-center">
#       <!-- Checkbox -->
#       <div class="form-check">
#         <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
#         <label class="form-check-label" for="form2Example31"> Remember me </label>
#       </div>
#     </div>
#
#     <div class="col">
#       <!-- Simple link -->
#       <a href="#">Forgot password?</a>
#     </div>
#   </div>
#
#   <!-- Submit button -->
#   <button type="button" class="btn btn-primary btn-block mb-4">Sign in</button>
#
#   <!-- Register buttons -->
#   <div class="text-center">
#     <p>Not a member? <a href="#">Register</a></p>
#     <p>or sign up with:</p>
#     <button type="button" class="btn btn-link btn-floating mx-1">
#       <i class="fab fa-facebook-f"></i>
#     </button>
#
#     <button type="button" class="btn btn-link btn-floating mx-1">
#       <i class="fab fa-google"></i>
#     </button>
#
#     <button type="button" class="btn btn-link btn-floating mx-1">
#       <i class="fab fa-twitter"></i>
#     </button>
#
#     <button type="button" class="btn btn-link btn-floating mx-1">
#       <i class="fab fa-github"></i>
#     </button>
#   </div>
# </form>
# * Sonra formda bazı değişiklikler yapacağız. Öncelikle sayfayı görüntüleyelim.

# ? 3. views.py
# * user appi içindeki views.py içerisinde sayfayı görüntüleyebilmek için
# * gerekli fonksiyonumuzu yazıyoruz.
# def loginPage(request):
#     return render(request,'login.html')

# ? 4. urls.py
# * newproject app içindeki urls.py içerisine pathi belirtiyoruz;
#      path('login/',loginPage,name='login'),
# * Artık sayfamızı http://127.0.0.1:8000/login/ adresinden görüntüleyebilmeliyiz.

# ? 5. form işlemleri
# * Django'da bir form ile çalışıyorsak formun 4 adet özelliği olmalı;
# * 1. formun metodu POST ya da GET olmalı. POST daha çok tercih edeceğiz. (bknz. notlar.py)
# * 2. {% csrf_token %} muhakkak olmalı. (bknz. notlar.py)
# * 3. inputların name'leri olmalı.
# * 4. button tipi muhakkak submit olmalı.
# * 5. Güncellenen haliyle formumuz;
#    <div class = "container" >
#        <div class = "row d-flex justify-content-center my-5" >
#            <div class = "col-9" >
#                <form method = "POST" > #* methodu ekledik
#                    { % csrf_token % } #* token ekledik
#                    <!-- user input - -> #* input nameler eklendi
#                    <div class = "form-outline mb-4" >
#                      <input name = "username" type = "text" id = "form2Example1" class = "form-control" / >
#                      <label class = "form-label" for = "form2Example1" > Kullanıcı Adı < /label >
#                    </div >
#
#                    <!-- Password input - ->
#                    <div class = "form-outline mb-4" >
#                      <input name = "password" type = "password" id = "form2Example2" class = "form-control" / >
#                      <label class = "form-label" for = "form2Example2" > Şifre < /label >
#                    </div >
#
#                    <!-- Submit button - -> #* type submit yaptık
#                    <button type = "submit" class = "btn btn-primary btn-block mb-4" > Giriş Yap < /button >
#
#                    <!-- Register buttons - ->
#                    <div class = "text-center" >
#                      <p > Hesabınız Yok mu? < a href = "#" > Hesap Oluştur < /a > </p >
#                      <p > Giriş Yap: < /p >
#                      <button type = "button" class = "btn btn-link btn-floating mx-1" >
#                        <i class = "fab fa-facebook-f" > </i >
#                      </button >
#
#                      <button type = "button" class = "btn btn-link btn-floating mx-1" >
#                        <i class = "fab fa-google" > </i >
#                      </button >
#
#                      <button type = "button" class = "btn btn-link btn-floating mx-1" >
#                        <i class = "fab fa-twitter" > </i >
#                      </button >
#
#                      <button type = "button" class = "btn btn-link btn-floating mx-1" >
#                        <i class = "fab fa-github" > </i >
#                      </button >
#                    </div >
#                  </form>
#            </div>
#        </div>
#    </div>

# ? 6. views içeriği
# * Öncelikle importlarımıızı yapalım. (bknz. importlar.py)
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User
# from django.contrib import messages
# import time
# * loginPage içeriğine eklemelerimizi yapıyoruz;
#    if request.method == "POST":#* eğer submit yapıldığında form methodu POST ise
#        username = request.POST.get("username")#* username değişkenine username inputundan alınan değeri atıyoruz
#        password = request.POST.get("password")#* password değişkenine password inputundan alınan değeri atıyoruz
#
#        user = authenticate(username=username, password=password)
#        #* authenticate fonksyironuyla kullanıcı adı ve şifrenin uyuşup uyuşmadığını kontrol ediyoruz
#        context = {}
#
#        if user is not None:#* Eğer kullanıcı yok değil ise(varsa):
#            login(request, user)#* kullanıcının bilgileriyle login fonksiyonunu çalıştırıyoruz
#            messages.success(request, 'Hoşgeldin '+ user.username + '!')#*başarılı giriş mesajı gönderiyoruz
#            return redirect('index')#* anasayfaya yönlendiriyoruz
#        else:#* eğer kullanıcı yok ise:
#            messages.warning(request, 'Kullanıcı adı veya şifre yanlış!!')#*hata mesajını veriyoruz
#            time.sleep(3)#*3 saniye sayfada bekletiyor
#            return redirect("login")#* login sayfasına tekrar yönlendirme yapıyoruz.
#
#    context = {}

# ? 7. mesajlar
# * Gönderilen  mesajların görüntülenebilmesi için bir mesaj alanı oluşturacağız.
# * base.html içerisine eklemeler yapacağız.
# * block style'ın hemen üst tarafına;
#    <style>
#        body {
#            font-family: 'Roboto', sans-serif;
#            background-color: rgb(28, 27, 27);
#            color: rgb(166, 173, 179);
#        }
#        .warning {
#            min-width: 200px;
#            height: 60px;
#            box-shadow: 2px 2px 4px #00000030;
#            border: 1px solid #00000030;
#            border-radius: 10px;
#            position: relative;
#            z-index: 2500;
#            background: #ffffff;
#            overflow: hidden;
#            animation: warning 5s linear both;
#            margin-bottom: 5px;
#        }
#        .warn {
#            padding: 10px;
#        }
#        .warn-time {
#            width: 100%;
#            height: 8px;
#            background: brown;
#            position: absolute;
#            bottom: 0;
#            animation: warntime 5s linear;
#        }
#        @keyframes warning {
#            80% {
#                opacity: 1;
#                z-index: 25;
#            }
#            100% {
#                opacity: 0;
#                z-index: -100;
#            }
#        }
#        @keyframes warntime {
#            100% {
#                width: 0px;
#            }
#        }
#    </style>
# * body etiketinin hemen altına ise;
#    <div style="position: absolute; top: 100px; right: 70px;">
#        {% if messages %}#* eğer gösterilecek mesaj var ise;
#        {% for i in messages %}
#        <div class="warning">
#            <div class="warn">{{ i }}</div>
#            <div class="warn-time" style="background: green;"></div>
#        </div>
#        {% endfor %}
#        {% endif %}
#    </div>
# * bu şekilde mesajları da artık görüntüleyebiliyoruz.

# ? 8. Admin panelden kullanıcı oluşturma-giriş yapma
# * Admin panel üzerinden bir kullanıcı oluşturuyoruz.
# * Bu kullanıcı adı ve şifresiyle login sayfamızı deniyoruz.

# ! Tebrikler! Artık login sayfamız hazır, giriş yapabiliyoruz!


