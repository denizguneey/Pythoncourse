#Fonksiyon kavramı ve önemi 
#Fonksiyonları tanımlama ve çalıştırma
#Parametre almayan ve alan fonksiyonlar 
#return anahtar kelimesi 
#parametrelere varsayılan değerler atamak

# def bilgi_ver():
#     print("işlem başarılı")
#     print("bloğun içerisi")

# bilgi_ver()



# def selamla():
#     print("merhaba")
# selamla()



# def selamla(isim):    fonksiyonun aldığı parametre
#     print("Merhaba "+isim)

# selamla("Deniz")


# def topla(x,y):
#     print(f"x+y={x+y}")
# topla(3,6)



# def carp(x,y):
#     print(f"x+y={x*y}")

# carp(3,6)



# def ort_hesapla(x,y):
#     print(f"(x+y)/2={(x+y)/2}")

# ort_hesapla(3,6)



# def ortalama_hesapla(liste):
#     toplam = sum(liste)
#     adet = len(liste)
#     ortalama = toplam/adet
#     print(f"Girilen sayıların ortalaması: {ortalama}")

# ortalama_hesapla([4,2,10])   



# def buyuk_harfe_cevir(metin):
#     metin=metin.upper()
#     print(metin)

# buyuk_harfe_cevir("deniz")



# def selamla(mesaj,isim):
#     print(f"{mesaj} {isim}.")

# selamla("Merhaba","Ahmet")


# def indirim_yap(fiyat,yuzde):
#     indirim_miktarı = fiyat *(yuzde/100)
#     indirimli_fiyat = indirim_miktarı
#     print(f"İndirimli tutar: {indirimli_fiyat}")

# indirim_yap(560,6)



# def topla(x,y):
#     print(x+y)
#     return x+y

# sonuc= topla(3,8)
# print(sonuc)    return kelimesi bize pythonda herhangi bir değeri geri döndürmesi anlamına geliyor



# def ortalama_hesapla(x,y):
#     return (x+y)/2
# print(type(ortalama_hesapla(3,7)))   float oldu




# def ortalama_hesapla(x,y):
#     return (x+y)/2
# a = ortalama_hesapla(2,6)
# b =ortalama_hesapla(6,10)
# print(a+b)          
#"return" bir fonksiyonda elde edilen sonucu bir değişkene atamak 
#ve tekrar kullanmak istiyorsak




# def buyuk_harfe_cevir(metin):
#     return metin.upper()
# print(buyuk_harfe_cevir("deniz"))




# import lesson11

# sonuc=lesson11.cember_cevresi(4)
# print(sonuc)

# from lesson11 import cember_cevresi

# sonuc = cember_cevresi(4)
# print(sonuc)


# import lesson11 as lesl
# sonuc = lesl.daire_alani(5)
# print(sonuc)


