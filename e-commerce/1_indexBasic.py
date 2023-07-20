
# ! ANASAYFA

# ? site ve ürünle ilgili sayfaları market appi içinde toplayacağız.
# ? mdBootstrap kullanacağız.

# ? 1. includes  
# * market appi içindeki templates klasörünün içine includes adında bir klasör açıyoruz.
# * navbar,footer gibi componentları burada oluşturacağız.
# * Tek bir noktada yapılan değişikliklerin tüm projeyi etkileyebilmesi için 
# * component mantığını kullanıyoruz. 

# ? 2. navbar
# * includes klasörü içine _navbar.html dosyası açıyoruz.
# * html içine aşağıdaki navbarı yapıştırıyoruz;

# <!-- Navbar -->
# <nav class="navbar navbar-expand-lg navbar-light bg-light">
#   <!-- Container wrapper -->
#   <div class="container-fluid">
    # <!-- Toggle button -->
    # <button
    #   class="navbar-toggler"
    #   type="button"
    #   data-mdb-toggle="collapse"
    #   data-mdb-target="#navbarSupportedContent"
    #   aria-controls="navbarSupportedContent"
    #   aria-expanded="false"
    #   aria-label="Toggle navigation"
    # >
    #   <i class="fas fa-bars"></i>
    # </button>
# 
    # <!-- Collapsible wrapper -->
    # <div class="collapse navbar-collapse" id="navbarSupportedContent">
    #   <!-- Navbar brand -->
    #   <a class="navbar-brand mt-2 mt-lg-0" href="#">
        # <img
        #   src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp"
        #   height="15"
        #   alt="MDB Logo"
        #   loading="lazy"
        # />
    #   </a>
    #   <!-- Left links -->
    #   <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        # <li class="nav-item">
        #   <a class="nav-link" href="#">Dashboard</a>
        # </li>
        # <li class="nav-item">
        #   <a class="nav-link" href="#">Team</a>
        # </li>
        # <li class="nav-item">
        #   <a class="nav-link" href="#">Projects</a>
        # </li>
    #   </ul>
    #   <!-- Left links -->
    # </div>
    # <!-- Collapsible wrapper -->
# 
    # <!-- Right elements -->
    # <div class="d-flex align-items-center">
    #   <!-- Icon -->
    #   <a class="text-reset me-3" href="#">
        # <i class="fas fa-shopping-cart"></i>
    #   </a>
# 
    #   <!-- Notifications -->
    #   <div class="dropdown">
        # <a
        #   class="text-reset me-3 dropdown-toggle hidden-arrow"
        #   href="#"
        #   id="navbarDropdownMenuLink"
        #   role="button"
        #   data-mdb-toggle="dropdown"
        #   aria-expanded="false"
        # >
        #   <i class="fas fa-bell"></i>
        #   <span class="badge rounded-pill badge-notification bg-danger">1</span>
        # </a>
        # <ul
        #   class="dropdown-menu dropdown-menu-end"
        #   aria-labelledby="navbarDropdownMenuLink"
        # >
        #   <li>
            # <a class="dropdown-item" href="#">Some news</a>
        #   </li>
        #   <li>
            # <a class="dropdown-item" href="#">Another news</a>
        #   </li>
        #   <li>
            # <a class="dropdown-item" href="#">Something else here</a>
        #   </li>
        # </ul>
    #   </div>
    #   <!-- Avatar -->
    #   <div class="dropdown">
        # <a
        #   class="dropdown-toggle d-flex align-items-center hidden-arrow"
        #   href="#"
        #   id="navbarDropdownMenuAvatar"
        #   role="button"
        #   data-mdb-toggle="dropdown"
        #   aria-expanded="false"
        # >
        #   <img
            # src="https://mdbcdn.b-cdn.net/img/new/avatars/2.webp"
            # class="rounded-circle"
            # height="25"
            # alt="Black and White Portrait of a Man"
            # loading="lazy"
        #   />
        # </a>
        # <ul
        #   class="dropdown-menu dropdown-menu-end"
        #   aria-labelledby="navbarDropdownMenuAvatar"
        # >
        #   <li>
            # <a class="dropdown-item" href="#">My profile</a>
        #   </li>
        #   <li>
            # <a class="dropdown-item" href="#">Settings</a>
        #   </li>
        #   <li>
            # <a class="dropdown-item" href="#">Logout</a>
        #   </li>
        # </ul>
    #   </div>
    # </div>
    # <!-- Right elements -->
#   </div>
#   <!-- Container wrapper -->
# </nav>
# <!-- Navbar -->

# ? 3. footer
# * includes klasörü içine _footer.html dosyası açıyoruz.
# * html içine aşağıdaki footerı yapıştırıyoruz;

# <!-- Footer -->
# <footer class="text-center text-lg-start bg-light text-muted">
    # <!-- Section: Social media -->
    # <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
    #   <!-- Left -->
    #   <div class="me-5 d-none d-lg-block">
        # <span>Get connected with us on social networks:</span>
    #   </div>
    #   <!-- Left -->
#   
    #   <!-- Right -->
    #   <div>
        # <a href="" class="me-4 text-reset">
        #   <i class="fab fa-facebook-f"></i>
        # </a>
        # <a href="" class="me-4 text-reset">
        #   <i class="fab fa-twitter"></i>
        # </a>
        # <a href="" class="me-4 text-reset">
        #   <i class="fab fa-google"></i>
        # </a>
        # <a href="" class="me-4 text-reset">
        #   <i class="fab fa-instagram"></i>
        # </a>
        # <a href="" class="me-4 text-reset">
        #   <i class="fab fa-linkedin"></i>
        # </a>
        # <a href="" class="me-4 text-reset">
        #   <i class="fab fa-github"></i>
        # </a>
    #   </div>
    #   <!-- Right -->
    # </section>
    # <!-- Section: Social media -->
#   
    # <!-- Section: Links  -->
    # <section class="">
    #   <div class="container text-center text-md-start mt-5">
        # <!-- Grid row -->
        # <div class="row mt-3">
        #   <!-- Grid column -->
        #   <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
            # <!-- Content -->
            # <h6 class="text-uppercase fw-bold mb-4">
            #   <i class="fas fa-gem me-3"></i>Company name
            # </h6>
            # <p>
            #   Here you can use rows and columns to organize your footer content. Lorem ipsum
            #   dolor sit amet, consectetur adipisicing elit.
            # </p>
        #   </div>
        #   <!-- Grid column -->
#   
        #   <!-- Grid column -->
        #   <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
            # <!-- Links -->
            # <h6 class="text-uppercase fw-bold mb-4">
            #   Products
            # </h6>
            # <p>
            #   <a href="#" class="text-reset">Angular</a>
            # </p>
            # <p>
            #   <a href="#" class="text-reset">React</a>
            # </p>
            # <p>
            #   <a href="#" class="text-reset">Vue</a>
            # </p>
            # <p>
            #   <a href="#" class="text-reset">Laravel</a>
            # </p>
        #   </div>
        #   <!-- Grid column -->
#   
        #   <!-- Grid column -->
        #   <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
            # <!-- Links -->
            # <h6 class="text-uppercase fw-bold mb-4">
            #   Useful links
            # </h6>
            # <p>
            #   <a href="#" class="text-reset">Pricing</a>
            # </p>
            # <p>
            #   <a href="#" class="text-reset">Settings</a>
            # </p>
            # <p>
            #   <a href="#" class="text-reset">Orders</a>
            # </p>
            # <p>
            #   <a href="#" class="text-reset">Help</a>
            # </p>
        #   </div>
        #   <!-- Grid column -->
#   
        #   <!-- Grid column -->
        #   <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
            # <!-- Links -->
            # <h6 class="text-uppercase fw-bold mb-4">Contact</h6>
            # <p><i class="fas fa-home me-3"></i> New York, NY 10012, US</p>
            # <p>
            #   <i class="fas fa-envelope me-3"></i>
            #   info@example.com
            # </p>
            # <p><i class="fas fa-phone me-3"></i> + 01 234 567 88</p>
            # <p><i class="fas fa-print me-3"></i> + 01 234 567 89</p>
        #   </div>
        #   <!-- Grid column -->
        # </div>
        # <!-- Grid row -->
    #   </div>
    # </section>
    # <!-- Section: Links  -->
#   
    # <!-- Copyright -->
    # <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
    #   © 2021 Copyright:
    #   <a class="text-reset fw-bold" href="https://mdbootstrap.com/">MDBootstrap.com</a>
    # </div>
    # <!-- Copyright -->
#   </footer>
#   <!-- Footer -->

# ? 4. base.html
# * templates klasörünün içerisine base.html adında bir dosya açıyoruz.
# * html iskeletini oluşturuyoruz. MdBootstrap için linklemeleri yapacağız.
# * head etiketleri içerisine css dosyalarını ekliyoruz;
# <!-- Font Awesome -->
# <link
#   href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
#   rel="stylesheet"
# />
# <!-- Google Fonts -->
# <link
#   href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
#   rel="stylesheet"
# />
# <!-- MDB -->
# <link
#   href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.4.0/mdb.min.css"
#   rel="stylesheet"
# />

# * Linklerin altına sayfalara css eklemek istediğimizde ayrıca kullanabilmek için style block açıyoruz;
    # {% block style %}
    # {% endblock style %}

# * body etiketi kapanışının hemen üzerine js dosyalarını ekliyoruz;
# <!-- MDB -->
# <script
#   type="text/javascript"
#   src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.4.0/mdb.min.js"
# ></script>

# * sayfaların adlandırmasını değiştirebilmek için head içindeki title etiketini
# * block içerisine alıyoruz;
    # {% block title %}
    # <title>Document</title>
    # {% endblock title %}

# * body tagi içine üst tarafa navbarı eklemek için;
#  {% include 'includes/_navbar.html' %}

# * navbar ve footer arasına sayfalarda değişiklik yapacağımız kısım için;
    # {% block main %}        
    # {% endblock main %}

# * body içine alt tarafa footerı eklemek için;
#  {% include 'includes/_footer.html' %}

# ? 5. index.html
# * Artık anasayfayı ayarlayacağız.
# * market/templates klasörüne index.html adında bir dosya açıyoruz.
# * Tüm componentları oluşturduğumuz için işimiz çok kolay artık. Aşağıdaki şekilde sayfa içeriğini hazırlıyoruz;

# * base.html içeriğini tamamen içe aktarıyoruz;
# {% extends 'base.html' %}

# * sayfa yüklenirken static dosyalarının düzgün çalışması için static dosyalarını yüklüyoruz;
# {% load static %}

# * sayfaya özel title içeriğini değiştiriyoruz;
# {% block title %}
# <title>Anasayfa</title>
# {% endblock title %}

# * title altına sayfalara css eklemek istediğimizde ayrıca kullanabilmek için style block açıyoruz;
# {% block style %}
# {% endblock style %}

# * sayfaya özel main kısmını oluşturuyoruz;
# {% block main %}
    # <p>Burası Anasayfa olacak.</p>
# {% endblock main %}
 
# ? 6. views ayarları
# * sayfayı görüntüleyebilmek için views ayarını yapıyoruz;
# def indexPage(request):
#     return render(request,'index.html')

# ? 7. urls ayarları
# * views dosyasındaki fonksiyonun yolunu burada belirteceğiz;
#   path('',indexPage,name='index'),
# * ilk parametre anasayfa olduğu için boş.
# * ikinci parametre fonksiyonumuzun adı.
# * üçüncü parametre ise sayfaya verdiğimiz isim kısmı.

# ? 8. Proje ayaklandırma
# * py manage.py runserver komutu ile projemizi ayaklandırıyoruz.

# ! Tebrikler! İlk sayfamızı artık görüntüleyebiliyoruz!
