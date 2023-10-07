#ekrandan alınan bir sayının faktöriyelini hesaplayan bir program yazınız
#input fonksiyonu

# sayi= input("Bir sayı giriniz: ")
# print(sayi)   output: girilen sayıyı yazdırıyor

# sayi= input("Bir sayı giriniz: ")
# print(type(sayi))  output: ekranda girilen sayıyı her zaman string görür

# sayi= input("Bir sayı giriniz: ")
# sayi=int(sayi)
# print(type(sayi))   output: int yapıldı

# sayi= int(input("Bir sayı giriniz: "))
# print(type(sayi)) output: int oldu

# sayi= int(input("Bir sayı giriniz: "))

# faktoriyel = 1

# for i in range(1, sayi + 1):
#     faktoriyel *= i
# print(f"{sayi}! = {faktoriyel}")  output:ekrandan alınan bir sayının faktöriyelini hesaplayan




# sayi= int(input("Bir sayı giriniz: "))
# faktoriyel = 1

# i=2
# while i<=sayi:
#     faktoriyel *=i
#     i += 1


# print(f"{sayi}! = {faktoriyel}")  output: ekrandan alınan bir sayının faktöriyelini hesaplayan bir program




#ekrandan alınan bir sayının asal olup olmadığını kontrol eden bir program yazınız.

# sayi= int(input("Bir sayı giriniz: "))

# prime=True
# for i in range(2,sayi):
#     if sayi %i ==0:
#         prime = False
#         break
# if prime == True:
#     print(f"{sayi} sayısı asaldır")
# else:
#     print(f"{sayi} sayısı asal değildir")    output: asal olup olmadığını kontrol etti



#ekrandan alınan bir sayının pozitif kaç tane böleni olduğunu bulan bir program yazınız

# sayi= int(input("Bir sayı giriniz: "))

# bolen_sayisi=0
# for i in range(1,sayi + 1):
#     if sayi %i ==0:
#         bolen_sayisi += 1
# print(f"{sayi} sayısının {bolen_sayisi} tane böleni vardır.")






#ekrandan okunan bir sayının rakamları toplamını hesaplayan bir program yazınız.

# sayi= int(input("Bir sayı giriniz: "))

# str_sayi = str(sayi)
# toplam = 0
# for rakam in str_sayi:
#     toplam += int(rakam)

# print(toplam)    output: str çevirerek yaptık





# sayi= int(input("Bir sayı giriniz: "))

# toplam = 0
# gecici_sayi = sayi

# while gecici_sayi != 0:
#     basamak = gecici_sayi %10
#     toplam += basamak
#     gecici_sayi //=10
# print(toplam)    output: sayıyı str çevirmeden yaptık basamak basamak


 

#ekrandan peşpeşe okunan 5 sayının en küçüğünü ve en büyüğünü ekrana yazdıran bir program yazınz.

# liste= []
# for i in range(5):
#     sayi= int(input("Bir sayı giriniz: "))
#     liste.append(sayi)
# print(f"en büyük sayı : {max(liste)}")
# print(f"en küçük sayı : {min(liste)}")



#ekrandan okunan bir sayının herhangi bir sayının karesi olup olmadığını kontrol eden bir program yazınız

# sayi= int(input("Bir sayı giriniz: "))
# karekok=sayi ** 0.5
# if karekok == int(karekok):
#     print("Tamkare")
# else:
#     print("Tamkare değil")  




#ekrandan okunan bir metinde hangi harfin kaç kere kullanıldığını gösteren bir program yazınız.

# metin= input("Bir metin giriniz: ")

# sozluk=dict()
# for harf in metin:
#     if harf in sozluk:
#         sozluk[harf] += 1
#     else:
#         sozluk[harf]=1
# for harf, adet in sozluk.items():
#     print(harf,adet)





#ekrandan okunan bir metinde a harflerini büyük yapan bir program yazınız.


# metin= input("Bir metin giriniz: ")
# metin2 = ""

# for harf in metin:
#     if harf =="a":
#         metin2 += "A"
#     else:
#         metin2 += harf
# print(metin2)