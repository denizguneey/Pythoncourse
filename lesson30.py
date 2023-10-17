#fonksiyonların parametreleri args, kwargs kullanımı

# def kuvvet_al(x,y):  ## Positional arguments (hepsi tam olarak girilmeli)
#     return x ** y

# print(kuvvet_al(3,4))

# def bilgi_ver(ad,soyad,yas):
#     return f"Ad: {ad} Soyadı: {soyad} Yaş: {yas}"
# print(bilgi_ver("Ali","Çalışkan",20))


# def bilgi_ver(ad,soyad = "Girilmedi" ,yas = "Girilmedi"):   ##Keyword argument
#     return f"Ad: {ad} Soyadı: {soyad} Yaş: {yas}"

# #print(bilgi_ver("Ali"))

# def bilgi_ver2(ad,soyad = "Girilmedi" ,yas = "Girilmedi"):   ##Keyword argument
#     return f"Ad: {ad} Soyadı: {soyad} Yaş: {yas}"
# print(bilgi_ver2("Ali",yas=34))


# def topla2(x,y):
#  return x+y

# def topla3(x,y,z):
#  return x+y+z

# def topla(*args): #istediğimiz kadar parametre girebiliriz
#     for arg in args:
#         print(arg)

#topla(1,2,3,4,5,"Python",True)

# def carp(*args):
#    carpim=1
#    for arg in args:
#       carpim *= arg
#    return carpim

# print(carp(2,3,523))

# def ortalama(*args):
#    return sum(args) / len(args)
# print(ortalama(6,10))


# def selamla(mesaj,*args):
#    sonuc=" "
#    sonuc += mesaj
#    sonuc+=" "
#    for arg in args:
#       sonuc+= arg
#       sonuc+=" "
#    return sonuc

# print(selamla("Merhaba", "Ali", "Nasılsın"))



# def fonk(**kwargs): #istediğimiz kadar keyword argument girebiliriz demek oluyor
#     print(kwargs)

# fonk(ad="Ali", soyad="Çalışkan", yas=34 )


# def fonk2(zorunlu,*args,**kwargs):
#     print(zorunlu)
#     print("********")
#     for arg in args:
#         print(arg)
#     print("********")
#     for kwarg in kwargs:
#         print(kwarg)
# fonk2(2,3,4,5,6,7,ad="Ali",yas=23)