#iç içe fonksiyon kullanımı

# def dis_fonk():
#   print("Dış Fonk Çalışıyor")
#   def ic_fonk():
#      print("İç Fonk Çalışıyor")
#   ic_fonk()
#   print("Dış Fonk Sonlanıyor")

# dis_fonk()


# def hesaplamalar(x):
#     def kare_al(a):
#         return a ** 2
#     def karekok_al(a):
#         return a ** 0.5
#     def faktoriyel(a):
#         carpim=1
#         for i in range (1,a+1):
#             carpim *= i
#         return carpim
#     kare = kare_al(x)
#     kaarekok=karekok_al(x)
#     fakt=faktoriyel(x)
#     return f"Karesi: {kare} Karekökü: {kaarekok} Faktöriyeli: {fakt}"

# print(hesaplamalar(6))



# def toplam_carpim(*args):
#     def toplama(demet):
#         return sum(demet)
#     def carpma(demet):
#         carpim=1
#         for i in demet:
#             carpim *= i
#         return carpim
#     return f"Toplamları: {toplama(args)} Çarpımları: {carpma(args)}"
# print(toplam_carpim(2,4,5))