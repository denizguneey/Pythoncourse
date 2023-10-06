#sözlük nedir?
#Sözlük nasıl oluşturulur?
#Sözlük nasıl yazdırılır?
#sözlükte verilere nasıl erişilir?
#sözlükte veriler nasıl değiştirilir?
#sözlükte birden fazla alan nasıl değiştirilir?
#sözlükten bir alan nasıl silinir?
#keys ve values ve items metotları
#sözlüğü for döngüsü yardımıyla nasıl yazdırabiliriz?
#"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]
#"book": "kitap", "black": "siyah", "cat":"kedi"


#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#print(kisi["isim"]) output: kişi sözlüğündeki ismin karşılığını getiriyor


#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#print(kisi)
#kisi["isim"]="Ahmet"
#print(kisi)  output: sözlükteki elemanları güncelleyebiliyoruz


#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#print(kisi)
#kisi.update({"isim":"Ahmet", "yas":30})
#print(kisi)      output: birden fazla alan değiştirme




#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#print(kisi)
#kisi["id"]=12345
#print(kisi)    output: sözlüğe yeni alan ekleme


#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#kisi["id"]=12345
#print(kisi)
#del kisi["id"]
#print(kisi)     output: bir alan silme



#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#for x in kisi:
#    print(x)   output: anahtar kısımlarını yazdırdı tek tek



#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#for x in kisi:
#    print(kisi[x])   output: değerlerini yazdırdı tek tek




#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}

#print(kisi.keys())   output: sadece anahatar kısımlarını yazdırdı




#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}

#print(kisi.values())   output: sadece değerleri yazdırdı



#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}

#print(kisi.items())    output: 2 li olarak eşleştirip yazdı



#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#for k in kisi.items():
#    print(k)   output: 2 li olarak tek tek yazdı



#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#for k,v in kisi.items():
#    print(k,v)     output: 2 tane değişken kullanabliriz


#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#print(kisi["id"])   output: hata veriyor eleman olmadığından



#kisi= {"isim":"ali", "yas":20, "cinsiyet":"m", "hobiler": ["Sinema", "Konser","Yazılım"]}
#print(kisi.get("id","Bulunamadı"))   output: hiç yok diyor hata vermiyor
#sözlükte girdiğimiz eleman yoksa vermesini istediğimiz mesaj "Bulanamadı" oluyor yani 2.kısım
