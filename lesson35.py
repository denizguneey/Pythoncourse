#Decorators (varolan fonksiyonlara özellikler eklemeye yarıyorlar)

# def decorator(fonk):
#     def wrapper():
#         print("fonksiyon çalışmadan önceki işlemler")
#         fonk()
#         print("fonksiyon çalıştıktan sonraki işlemler")
#     return wrapper

# @decorator
# def fonksiyon():
#     print("fonksiyon çalışıyor")

# fonksiyon()


# import time

# def zaman_hesapla(fonk):
#     def wrapper(*args,**kwargs):
#         baslangıc=time.time()
#         fonk(*args,**kwargs)
#         bitis=time.time()
#         print(f"işlem {bitis-baslangıc} saniye sürdü.")
#     return wrapper

# @zaman_hesapla
# def kareleri_al(liste):
#     for i in liste:
#         print(i*i)

# @zaman_hesapla
# def kupleri_al(liste):
#     for i in liste:
#         print(i**3)

# @zaman_hesapla
# def topla(a,b):
#     time.sleep(1)
#     print(a+b)

# kareleri_al(range(20))



# import time
# def zaman_hesapla(fonk):
#     def wrapper(*args,**kwargs):
#         baslangic=time.time()
#         sonuc=fonk(*args,**kwargs)
#         bitis=time.time()
#         print(f"işlem {bitis-baslangic} saniye sürdü.")
#         return sonuc
#     return wrapper

# @zaman_hesapla
# def kareleri_al(liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(i*i)
#     return sonuc
# @zaman_hesapla
# def kupleri_al(liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(i**3)
#     return sonuc
# @zaman_hesapla
# def topla(*args):
#     time.sleep(1)
#     return sum(args)

# print(kareleri_al(range(10)))
        
