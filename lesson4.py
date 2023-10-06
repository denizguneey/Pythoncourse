#Tuple (Demet) nedir?
#Tuple ve List yapılarının farkı ve benzerlikleri
#"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"

#demet=("Sarı", "Mavi","Yeşil","Kırmızı","Siyah")

#print(type(demet))   output: cinsi tuple



#demet=("Sarı", "Mavi","Yeşil","Kırmızı","Siyah")

#print(len(demet))  output: listede kaç eleman varsa onu söyler 5


#demet=("Sarı", "Mavi","Yeşil","Kırmızı","Siyah")

#demet(2)= "Pembe"  output: çalışmıyor dolayısıyla listelerden farkı 
#demet nasıl oluşturulduysa o şekilde kalır elemanları değiştiremeyiz


#demet=("Sarı", "Mavi","Yeşil","Kırmızı","Siyah")

#print(demet)

#Küme nedir ve nasıl tanımlanır?
#Kümeleri yazdırma
#Kümelere eleman ekleme-silme
#remove ve discard metotlarının farkı

#kume={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#print(type(kume))   output: set 

#kume={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#print(len(kume))   output: 5



#kume={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}

#for renk in kume:
#    print(renk)    output: her çalıştırıldığında farklı sıra geliyor
#bunun nedeni kümelerin sırasız yapıya sahip olması

#kume={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#print(kume)

#kume.add("Pembe")
#print(kume)    output: kümeye farklı sıralara gelecek şekilde pembe eklendi



#kume={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#print(kume)

#kume.remove("Sarı")
#print(kume)      output: Sarı gitti kümeden



#discard fonk

#kume={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#print(kume)

#kume.discard("Mavi")
#print(kume)       output: Discard fonk remove ile aynı 
#fakat remove fonk kümeye ait olmayan eleman çıkarılmaya çalışılırsa hata verir discard da küme olduğu gibi yazdırılır



#Kümelerde Kesişim ve Birleşim işlemi
#Kümelerde fark işlemi
#in anahtar kelimesi

#kume1={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#kume2={"Sarı", "Mavi","Yeşil","Beyaz","Gri"}

#print(kume1.intersection(kume2))   output: intersection veriyor


#kume1={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#kume2={"Sarı", "Mavi","Yeşil","Beyaz","Gri"}

#print(kume1.union(kume2))   output: birleşimi veriyor



#kume1={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#kume2={"Sarı", "Mavi","Yeşil","Beyaz","Gri"}

#print(kume1.difference(kume2))   output: küme1 de olup küme2 de olmayanlar


#kume1={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#kume2={"Sarı", "Mavi","Yeşil","Beyaz","Gri"}

#print("Sarı" in kume1)  output: elemanın kümede olup olmadığını kontrol eder


#kume1={"Sarı", "Mavi","Yeşil","Kırmızı","Siyah"}
#kume2={"Sarı", "Mavi","Yeşil","Beyaz","Gri"}

#print("Sarı" in kume1.union(kume2))  output: kümelerin birleşimi elemanı içeriyor mu

bosliste1=[]
bosliste2=list()

bosdemet1=()
bosdemet2=tuple()

boskume1=set()
#boskume2={}  bu bir boş küme değil sözlüktür

#python=set("PYTHON")
#print(python)   output: elemanları ayrı ayrı yazıyor farklı sırada
