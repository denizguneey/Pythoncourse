#Liste nedir ve nasıl oluşturulur?
#Liste nasıl yazdırılır?
#Len fonksiyonu nedir?
#Liste elemanlarına nasıl erişilebilir?
#Liste nasıl parçalanır?

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(type(renkler))   tipini öğrenmek için = liste

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler)   listedekileri yazdırmak için 

#stringlerde aslında karakterlerden oluşan bir liste


#len fonksiyonu (listede kaç eleman olduğunu söyleyen fonksiyon)

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(len(renkler))  output 5 geliyor




#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler[0]) output ilk eleman yani SİYAH geliyor




#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler[2:]) 2. indeksten başlayıp sona kadar yazdırma anlamına geliyor




#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler[1:4]) 1. indeksten başlayıp 3. ye kadar yazdırıyor 4 ü dahil etmiyor



#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler[::2])  2 şer 2 şer yazdırma



#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler[1:4:2])  1. den sonuncuya kadar 2 şer atlayıp yazdırma


#append metodu
#insert metodu
#remove metodu 
#extend metodu
#pop metodu
#reverse metodu
#sort ve sorted metotları

#append metodu liste sonuna eleman eklemeye yarar

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler)

#renkler.append("Gri")

#print(renkler)   output ilk renkler sonra gri eklenmesi ile renkler



#insert metodu araya eleman ekleme

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler)

#renkler.insert(0,"Gri")

#print(renkler)  output ilk elemana gri eklendi


#remove metodu listeden eleman silmeye yarar

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler)

#renkler.remove("Sarı")

#print(renkler)  output renkler sonra sarı kaldırılmış hali




#extend metodu araya birden fazla eleman ekleme

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#renkler2 = ["Turuncu", "Pembe"]

#renkler.append(renkler2)
#print(renkler)  output: listenin sonuna olduğu gibi ekliyor

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#renkler2 = ["Turuncu", "Pembe"]

#renkler.extend(renkler2)

#print(renkler)  output: listenin sonuna olduğu gibi eklemedi parantezsiz


#pop metodu bir listenin en son elemanını siliyor 

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler)

#renkler.pop()

#print(renkler)   output: listeden son eleman Yeşili attı



#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#print(renkler)

#silinen = renkler.pop()

#print(renkler)
#print(silinen)   output: son satırda silinende veriiyor


#reverse metodu listeyi tersine çeviren metot

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(renkler)
#renkler.reverse()
#print(renkler)    output: tersten yazdı listeyi


#sort metotu listeyi alfabetik olarak sıralıyor, eğer
#listenin içinde sayısal değerler varsa küçükten büyüğe sıralar

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(renkler)
#renkler.sort()
#print(renkler)   output: listeyi alfabetik sıraladı


#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(renkler)
#renkler.sort()
#renkler.reverse()
#print(renkler)   output: listeyi tersten alfabetik sıralar

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(renkler)
#renkler.sort(reverse=True)
#print(renkler)   output: listeyi tersten alfabetik sıralar daha kolay

#sorted fonksiyonu(metodu) listenin bozulmasını istemiyorsak sıralarken

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(renkler)
#liste2=sorted(renkler)
#print(liste2)
#print(renkler)    output: 3 satır 1. ve 3. satır aynı 2. sıra sıralı



#min,max ve in kullanımı
#sum kullanımı
#for döngüsü ile listeyi yazdırmak
#enumarate
#listeyi stringe çevirmek ve join metodu
#stringi listeye çevirmek ve split metodu

#min ve max metotları

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#sayılar=[1,2,39,4,3,7,8]
#print(min(renkler))  output: listede alfabetik olarak en küçük değer Beyazı aldı
#max içinde alfabetik en büyüğü seçiyor


#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#sayılar=[1,2,39,4,3,7,8]
#print(min(sayılar))  output: sayılar içerisinde en küçük değer 1i aldı
#max içinde sayılardan en büyüğü seçiyor


#sum metodu

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]

#sayılar=[1,2,39,4,3,7,8]
#print(sum(sayılar))  output: liste içindeki sayıları topladı



#for döngüsü

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#for i in renkler:
#    print(i)    output: renkleri teker teker yazdırma

#enumarate fonk bir listeyi numaralandırıyor

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(list(enumerate(renkler)))  output: numaralandırdı 0 dan başlayarak


#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print(list(enumerate(renkler,start=3)))  output: numaralandırmaya 3 ten başladı

#in fonk listede olup olmadığını kontrol etme

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#print("Siyah" in renkler)   output: True



#listeyi tek bir metin dosyası haline çevirme stringe join ile

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#stringrenkler = "".join(renkler)
#print(stringrenkler)  output: SiyahBeyazSarıMaviYeşil
#birleştirerek yazdı


#stringi listeye çevirmek ve split metodu


#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#stringrenkler = "-".join(renkler)
#print(stringrenkler)
#renkler2=stringrenkler.split("-")
#print(renkler2)   output: ayrı ayrı yazdı liste halinde
