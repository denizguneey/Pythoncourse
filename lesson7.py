#listeler ile for döngüsü
#range fonk ve for döngüsü
#iç içe for döngüleri
#break ve continue anahtar kelimeleri
#while döngüsü


# liste = [1,2,3,4,5,6]

# for rakam in liste:
#     print(rakam)  output: teker teker yazdırıyor
    



# isim = "Ahmet"

# for harf in isim:
#     print(harf)     output: harfleri tek tek yazdırdı


#range fonk

# for i in range(0,10):
#     print(i)  output: 10 dahil değil 10 a kadar yazdırdı




# for i in range(3,10,2):
#     print(i)   output:3 ten başlayıp 10u dahil etmeden 10 a kadar 2şer yazdırdı

# for i in range(10):
#     print(i)  output:  for i in range(0,10): bununla aynı anlama geliyor


# sonuc = 1
# for i in range(0,10):
#     sonuc *=2
# print(sonuc)  output: 2 üzeri 10 yani 1024 geldi
#BİR İŞLEMİ BELİRLİ SAYIDA TEKRARLATMAK İÇİN KULLANILIYOR



# liste1= ["a","b","c"]
# liste2=[1,2,3]

# for harf in liste1:
#     for rakam in liste2:
#         print(harf,rakam)




# liste=[1,2,3,4,5,6,7,8,9]
# for i in liste:
#     if i==3:
#         continue
#     print(i)    output: herhangi bir sayıyı yazdırmadan devam etmesini istiyorsak


# liste=[1,2,3,4,5,6,7,8,9]
# for i in liste:
#     if i==3:
#         break
#     print(i)   output: yazdırmak istemediğim yere kadar yazdırıyor 
# "break" fonk döngüyü sonlandırıyor
#"continue" fonk ise döngünün bir sonraki adımından devam etmesi için kullanılıyor

# liste = range(100)
# for i in liste:
#     if i %3 != 0:
#         continue
#     print(i)   output: 3 e tam bölünenleri yazdırdık döngü ile


# liste = range(100)
# for i in liste:
#     if i %3 != 0:
#         continue
#     if i==81:
#        break 
#     print(i)  output: 81 ve 81 den sonrakileri yazdırmasını istemedik


#while döngüsü belirli bir koşul sağlandığı sürece çalışan döngü

# x=2
# while x<10:
#     print(x)
#     x += 1   output: 1 er arttırarak 10 dan küçük rakamları yazdırdı
   

# x=2
# while x<10:
#     print(x)
#     x += 1
# print("x =",x)   output: sınırını gösterdik



# x=2
# y=3

# while x*y < 1000:
#     print(x,y)
#     x += 2
#     y += 2  output: verdiğimiz 2 sayıyı 2 şer arttırarak çarpımları 1000 e kadar olan sayıları yazdırdık




# i=1
# while True:
#     print(i)
#     i +=1  output: sürekli 1 er arttırarak yazdırır


# i=1
# while True:
#      print(i)
#      i +=1 
#      if i==10000:
#           break     output: 10000 e kadar yazdırdı



# i=1
# while True:
#     if i%2==0:
#         i +=1
#         continue
#     print(i)
#     i +=1
#     if i==1000:
#         break   output: 1000 e kadar tek sayıları yazdırdık












