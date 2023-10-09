#random, uniform fonksiyonları
#randint ve randrange fonksiyonları
#choice, shuffle ve sample fonksiyonları


#random modülü bizim için rastgele sayılar veya 
#değerler üreten fonksiyonları barındırıyor

# import random

# for i in range(10):
#     print(random.random())
#0 ile 1 arasında rastgele sayılar 10 tane

# import random

# for i in range(10):
#     print(random.uniform(10,30))
#10 ile 30 arasında belirlenen rastgele 10 sayı




# import random

# for i in range(10):
#     print(random.randint(1,5))
#1 ile 5 arasında rastgele 10 tam sayıyı veriyor bu sefer ilk değer dahil



# import random

# for i in range(10):
#     print(random.randrange(1,10,3))
#belirli aralıkta belirli sayıda artan rastgele 10 tam sayı
#2 parametre ile çalıştığında diğerlerinden bir farkı kalmıyor


# import random

# liste = ["Siyah", "Beyaz", "Mavi","Yeşil","Gri","Turuncu"]
# print(random.choice(liste))
#verilen bir listeden rastgele eleman seçiyor


# import random

# liste = ["Siyah", "Beyaz", "Mavi","Yeşil","Gri","Turuncu"]
# random.shuffle(liste)
# print(liste)
#listeyi karıştırıyor


# import random

# liste = ["Siyah", "Beyaz", "Mavi","Yeşil","Gri","Turuncu"]

# print(random.sample(liste,3))
#Listeden seçilecek eleman sayısı kadar rastgele eleman karıştırıyor





# import random

# zarlar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

# for i in range(100):
#     zar=random.randint(1,6)
#     zarlar[zar] += 1

# for zar in zarlar:
#     print(f"{zar} gelme olasılığı: {zarlar[zar] / 100}")
#100 zar atıldığında 1 den 6 ya kadar gelme olasılıkları



#10 kere 6-6 gelmesi için kaç sefer zar atılması gerek

# import random

# alti_alti=0
# deneme_sayisi=0
# while True:
#     deneme_sayisi += 1
#     zar1 =random.randint(1,6)
#     zar2 = random.randint(1,6)
#     if zar1 == 6 and zar2 ==6:
#         alti_alti += 1
#     if alti_alti == 10:
#         print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı ")
#         break