
# ! NAVBAR KULLANICI DÜZENLEME

# ? 1. Navbar sağ taraf düzenleme
# * Kullanıcı girişli olduğunda profil bilgilerinin görüntülenmesi,
# * kullanıcı girişli olmadığında giriş yapma sayfasının görünmesi gerekli.
# * Bunun için navbar üzerinde if yapısı kullanarak biraz değişiklik yapacağız.
# * Kodlarımızı aşağıdaki gibi güncelliyoruz;
#      {% if request.user.is_authenticated %} #*  <!-- ! user girişliyse -->
#      <!-- Right elements -->
#      <div class="d-flex align-items-center">
#        <h6 class="m-auto me-2" >{{ user.username }}</h6> #* user bilgisi
#        <!-- Icon -->
#        <a class="text-reset me-3" href="#">
#          <i class="fas fa-shopping-cart"></i>
#        </a>
#        <!-- Notifications -->
#        <div class="dropdown">
#          <a
#            class="text-reset me-3 dropdown-toggle hidden-arrow"
#            href="#"
#            id="navbarDropdownMenuLink"
#            role="button"
#            data-mdb-toggle="dropdown"
#            aria-expanded="false"
#          >
#            <i class="fas fa-bell"></i>
#            <span class="badge rounded-pill badge-notification bg-danger">1</span>
#          </a>
#          <ul
#            class="dropdown-menu dropdown-menu-end"
#            aria-labelledby="navbarDropdownMenuLink"
#          >
#            <li>
#              <a class="dropdown-item" href="#">Some news</a>
#            </li>
#            <li>
#              <a class="dropdown-item" href="#">Another news</a>
#            </li>
#            <li>
#              <a class="dropdown-item" href="#">Something else here</a>
#            </li>
#          </ul>
#        </div>
#        <!-- Avatar -->
#        <div class="dropdown">
#          <a
#            class="dropdown-toggle d-flex align-items-center hidden-arrow"
#            href="#"
#            id="navbarDropdownMenuAvatar"
#            role="button"
#            data-mdb-toggle="dropdown"
#            aria-expanded="false"
#          >
#            <img
#              src="https://mdbcdn.b-cdn.net/img/new/avatars/2.webp"
#              class="rounded-circle"
#              height="25"
#              alt="Black and White Portrait of a Man"
#              loading="lazy"
#            />
#          </a>
#          <ul
#            class="dropdown-menu dropdown-menu-end"
#            aria-labelledby="navbarDropdownMenuAvatar"
#          >
#            <li>
#              <a class="dropdown-item" href="#">Profilim</a>
#            </li>
#            <li>
#              <a class="dropdown-item" href="#">Ürünlerim</a>
#            </li>
#            <li>
#              <a class="dropdown-item" href="/logout">Çıkış Yap</a> #* logout fonksiyonu
#            </li>
#          </ul>
#        </div>
#      </div>
#      {% else %}#* <!-- !user girişli değilse -->
#      <div>
#        <div class="btn btn-danger">
#          <a href="{% url 'login' %}">Giriş Yap</a> #* login sayfasına yönlendirme
#        </div>
#      </div>
#      {% endif %}
# * Navbar ile sayfalar eklendikçe başka değişiklikler yapacağız.
