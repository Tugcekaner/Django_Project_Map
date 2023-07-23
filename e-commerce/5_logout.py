
# ! LOGOUT

# ? 1. views.py
# * Kullanıcının çıkış yapmasını sağlayacak olan fonksiyonu yazıyoruz.
#def logoutUser(request):
#    logout(request)
#    return redirect("login")

# ? 2. urls.py
# * urls.py'a path'i oluşturuyoruz.
#    path('logout',logoutUser,name='logout'),

# ? 3. navbara linkleme
# * navbar profil dropdown içeriğini güncelliyoruz;
#    <li>
#      <a class="dropdown-item" href="#">Profilim</a>
#    </li>
#    <li>
#      <a class="dropdown-item" href="#">Ürünlerim</a>
#    </li>
#    <li>
#      <a class="dropdown-item" href="/logout">Çıkış Yap</a>#* logout fonksiyonuna yönlendirdik
#    </li>

# ! Tebrikler! Artık kullanıcı sitenizden çıkış yapabiliyor!

