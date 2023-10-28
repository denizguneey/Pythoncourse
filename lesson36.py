#OOP property,setter,deleter decarator kullanımı

class Kisi:
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
        self.adsoyad=ad+" "+soyad

    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"
    
kisi1=Kisi("Ali","Uzun")
kisi1.ad="Ahmet"

print(kisi1.ad)
print(kisi1.adsoyad)
print(kisi1.email())