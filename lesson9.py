#Genel tekrar ve alıştırmalar


#ilk 10.000 asal sayının kaç tanesi 3 ile başlar ve 7 ile biter?

# prime_list = list()
# prime_list.append(2)

# sayi=3

# while True:
#     prime = True
#     for i in range(2,sayi):
#         if sayi %i == 0:
#             prime = False
#             break
#     if prime:
#         prime_list.append(sayi)
#         if len(prime_list) == 10000:
#             break
#     sayi += 1
# print(prime_list)   output: 1000 asal sayıyı yazdırıyor
    








# prime_list = list()
# prime_list.append(2)

# sayi=3

# while True:
#     prime = True
#     for i in range(2,sayi):
#         if sayi %i == 0:
#             prime = False
#             break
#     if prime:
#         prime_list.append(sayi)
#         if len(prime_list) == 100:
#             break
#     sayi += 1
# liste2=[]
# for prime in prime_list:
#     strprime = str(prime)
#     if strprime.startswith("3") and strprime.endswith("7"):
#         liste2.append(prime)
# print(liste2)
# print(len(liste2))    output: ilk 100 asal sayının içerisinde 3 ile başlayıp 7 ile bitenler





# prime_list = list()
# prime_list.append(2)

# sayi=3

# while True:
#     prime = True
#     for i in range(2,int(sayi**0.5)+1):
#         if sayi %i == 0:
#             prime = False
#             break
#     if prime:
#         prime_list.append(sayi)
#         if len(prime_list) == 10000:
#             break
#     sayi += 1
# liste2=[]
# for prime in prime_list:
#     strprime = str(prime)
#     if strprime.startswith("3") and strprime.endswith("7"):
#         liste2.append(prime)
# print(liste2)
# print(len(liste2))    output: 10000 asal sayı içinde 3 ile başlayıp 7 ile biten daha hızlı hesaplaması için





#3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir?

# for i in range(100,1000):
#     toplam=0             
#     gecici_sayi = sayi
#     while gecici_sayi != 0:  geçici sayı 0 olmadığı sürece
#         basamak = gecici_sayi % 10     10 ile bölümünden kalana baktık(birler bs aldık)
#         toplam += basamak ** 3    toplamı birler bs küpü kadar arttırdık
#         gecici_sayi //= 10     geçici sayıyı 10 a böldük



# liste=[]
# for sayi in range(100,1000):
#     toplam=0
#     gecici_sayi = sayi
#     while gecici_sayi != 0:
#         basamak = gecici_sayi % 10
#         toplam += basamak ** 3
#         gecici_sayi //= 10
#     if toplam == sayi:
#         liste.append(sayi)

# print(liste)      output: 153,370,371,407


#fibonacci sayı dizisi ilk iki terimi 1 olan ve sonraki her terimi kendisinden 
#önceki 2 terimin toplamı olan bir sayı dizisidir. ilk 100 fibonacci sayısını ekrana yazdırın.
#1,1,2,3,5,8,13,21,...

# fibonacci_list = []
# fibonacci_list.append(1)
# fibonacci_list.append(1)

# index = 2
# while True:
#     fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#     index += 1
#     if len(fibonacci_list) == 100:
#         break

# print(fibonacci_list)   output: çıkıyor hepsi while döngüsü ile olan




# fibonacci_list = []
# fibonacci_list.append(1)
# fibonacci_list.append(1)
# for i in range(2,100):
#     fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
 
# print(fibonacci_list)    output: for döngüsü ile



#100 basamaklı ilk fibonacci sayısını ekrana yazdırın

# fibonacci_list=list()
# fibonacci_list.append(1)
# fibonacci_list.append(2)

# index = 2
# while True:
#     fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#     terim =fibonacci_list[index-2]+fibonacci_list[index-1]
#     if len(str(terim))==100:
#         print(terim)
#         print(index)   kaçıncı sıradaki sayının 100 bs olduğunu öğrenmek için
#         break 
#     index += 1       aynı sayının eklenmemesi için










