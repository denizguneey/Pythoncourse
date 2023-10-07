# if ile kullanılacak operatörler
# Eşittir "==", Eşit değildir "!=", Büyüktür ">", Küçüktür "<", Büyük veya Eşittir ">=" Küçük veya eşittir "<="
#in anahtar kelimesi
#not anahtar kelimesi
#and ve or bağlaçları
#is anahtar kelimesi (Hafızada aynı nesne olmalı)

#a = 5
#b = 5
#if a==b:
#    print("a=b")   output: a=b geliyor


#a = 10
#b = 5
#if a>b:
#    print("a>b")   output: a>b geliyor

#a = 6
#b = 5
#if a != b:
#    print("a != b")   output: a != b geliyor


#a = 6
#b = 6
#if a==b:
#    print("a = b")
#else:
#    print("a != b")


#renk="Siyah"
#if renk=="Beyaz":
#    print("Beyaz")
#elif renk == "Sarı":
#    print("Sarı")
#elif renk=="Mavi":
#    print("Mavi")
#else:
#    print("Hiçbiri")    output: Hiçbiri



#a = 5
#b = 8
#c = 10
#if a<b or c>a:
#    print("koşul doğru")
#else:
#    print("koşul yanlış")  output: koşul doğru


#a = 5
#b = 8
#c = 10
#if a<b or c=a:
#    print("koşul doğru")
#else:
#    print("koşul yanlış")  output: koşul doğru bir tanesini sağlaması yeterli "or" olduğundan


#a = 5
#b = 8
#c = 10
#if a<b and b<c:
#    print("koşul doğru")
#else:
#    print("koşul yanlış")  output: koşul doğru her ikisinide sağlaması gerek "and" olduğundan


#liste = [1,2,3,4,5,6,7,8,9]
#a=4
#if a in liste:
#    print("Listede var")
#else:
#    print("Listede yok")   output: (listede var) olup olmadığını kontrol eder "in" fonk





#isim ="Python"
#a="P"
#if a in isim:
#    print("Listede var")
#else:
#    print("Listede yok") output: Listede var



#isim="Python"
#a="P"
#if not a in isim:
#    print("Listede var")
#else:
#    print("Listede yok") output:listede yok "not" fonk olduğundan


#a=8
#b=10
#if not a==b:
#    print("Koşul doğru")
#else: 
#    print("koşul yanlış")   output: koşul doğru


#a= "python"
#b= "pytho"
#b += "n"
#print(a)
#print(b)   output: python, python ikiside


#a= "python"
#b= "pytho"
#b += "n"
#if a==b:
#    print("a=b")
#else:
#    print("a !=b")   output: a=b




#a= "python"
#b= "pytho"
#b += "n"
#if a is b:
#    print("a=b")
#else:
#    print("a !=b")   output: a != b geldi çünkü "is" fonk detaylı bakarak karakterlerin aynı olmadığını gördü




#a= "python"
#b= "pytho"
#b += "n"
#if a is b:
#    print("a=b")
#else:
#    print("a !=b")
#    print(id(a))
#    print(id(b))   output: hafızada bulundukları adresler aynı çıkmıyor
