#time modülü

# import time
# zaman= time.time()
# print(zaman)
#1 ocak 1970ten beri geçen zamanın saniye cinsinden değeri

# import time
# baslangıc = time.time()
# liste =[]
# for i in range(100000):
#     liste.append(i)
# bitis = time.time()
# print(bitis-baslangıc)   bir işin yapılma süresi hesaplanırken




# import time

# zaman = time.ctime()
# print(zaman)   şu anki zamanı veriyor
  


# import time

# zaman = time.ctime(100000000)
# print(zaman)   başlangıçtan itibaren verilen saniyeden itibaren geçen zaman



# import time

# zaman = time.ctime()
# print(type(zaman))  tipi string



# import time

# zaman = time.localtime()
# print(zaman)   zamanları sınıflandırıp yazdırıyor ayrı ayrı



# import time

# zaman = time.asctime()
# print(zaman)    ctime aynısı şuanın tarihini veriyor


# import time

# zaman = time.strftime("%d:%m")
# print(zaman)   şu an ki gün ve ayı yazdırdık ctrl yapıp içerisindeki 
#gün ay yıl saat saniye fonk çalıştırılma şekline göre yazdırabiliriz

# import time

# print("Program başlatıldı")
# time.sleep(3)
# print("Program sonlandı")  kodun belirli bir süre uyumasını sağlıyor
