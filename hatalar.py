
# ! EN ÇOK ALINAN HATALAR

# * sayfa görünmüyorsa: html adı-url views adı farklı

# * sayfa görünmüyorsa: templates klasörü yeri yanlış, adı yanlış, urls içinde pathler arası virgül unutulması

# * noreversematch hatası : yönlendirme yanlış, pathlere-parametrelere bak

# * page not found(yönlendirmedeyse) yönlendirme içinde başta / yoksa hata verir

# * static ilk başta okumuyor, projeyi kapatıp runserver yapmak

# * css okumuyorsa önbelleğe takılmıştır (ctrl+f5) - localhostta çalışma kaynaklı

# * terminalde kırmızı unapplied migrations hatası: py manage.py migrate komutu

# * fielderror: field hatası, varsa forms.py kontrol edilmeli

# * kategorilerde hata aldığımızda kategori tekrarı söz konusu olabilir. Bunun çözümü birine related_name değeri vermek.

# * unboundlocal error: search yüzünden hata, index içindeki fonksiyon öncesinde dışarıda boş tanımlı search olması gerekiyor.

# * AttributeError: Bu hata, Python nesnelerinde olmayan bir nitelik (attribute) veya yöntem çağrılmaya çalışıldığında 
# * meydana gelir. İlgili nesne veya sınıfın doğru şekilde tanımlandığından emin olmak gerekir.

# * ImportError: Bu hata, Python'un modülleri veya paketleri içe aktarırken dosyanın veya paketin bulunamamasından kaynaklanır. 
# * Modül veya paketin var olduğundan ve doğru şekilde yüklendiğinden emin olunmalıdır.

# * KeyError: Bu hata, sözlüklerde anahtarların eksik veya yanlış adlandırıldığı durumlarda oluşur. Anahtarların var olduğundan 
# * ve doğru şekilde belirtildiğinden emin olunmalıdır.

# * ValueError: Bu hata, bir işlev veya metodun geçersiz bir değerle çağrılması durumunda meydana gelir. 
# * İşlevlere veya metodlara doğru türde ve geçerli değerlerin verildiğinden emin olunmalıdır.

# * IndentationError: Bu hata, Python kodunun girintileme (indentation) düzenlemesinin yanlış olması durumunda oluşur. 
# * Python'ın girintiye dayalı bir dil olduğundan, kod bloklarını doğru şekilde hizalamak önemlidir.

# * Internal Server Error (500): Django uygulamanızda bir hata olduğunda genellikle sunucu hatası olarak karşımıza çıkar. 
# * Django hata ayıklama özelliği açıkken daha ayrıntılı hata bilgilerini görebilirsiniz.

# * TypeError: Bu hata, işlevlere yanlış türde argümanlar geçirildiğinde veya uygun olmayan türde operasyonlar yapıldığında 
# * oluşur. Veri türlerinin uygun şekilde eşleştiğinden emin olunmalıdır.

