# #inheritance-kalıtım1

# class Calisan:
#     zam_orani=1.1
#     def __init__(self,isim,soyisim,maas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.maas=maas
#         self.email=isim + soyisim + "@sirket.com"
#     def bilgileri_soyle(self):
#         return "Ad: {} Soyadı: {} Maaş: {} Email: {}".format(self.isim,self.soyisim,self.maas,self.email)

# calisan1=Calisan("Ali","Çalışkan",5000)
# calisan2=Calisan("Veli","Uzun",6000)

# class Yazilimci(Calisan):
#     def __init__(self, isim, soyisim, maas,bildigi_dil):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.maas=maas
#         self.email=isim + soyisim + "@sirket.com"
#         self.bildigi_dil=bildigi_dil

#     def bilgileri_soyle(self):
#         return "Ad: {} Soyadı: {} Maaş: {} Email: {} Dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
        

# yazilimci1=Yazilimci("Ayşe","Yıldız",7000,"Python")
# yazilimci2=Yazilimci("Fatma","Ay",8000,"Java")

# print(calisan1.bilgileri_soyle())
# print(yazilimci1.bilgileri_soyle())







# class Calisan:
#     zam_orani=1.1
#     def __init__(self,isim,soyisim,maas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.maas=maas
#         self.email=isim + soyisim + "@sirket.com"
#     def bilgileri_soyle(self):
#         return "Ad: {} Soyadı: {} Maaş: {} Email: {}".format(self.isim,self.soyisim,self.maas,self.email)

# calisan1=Calisan("Ali","Çalışkan",5000)
# calisan2=Calisan("Veli","Uzun",6000)

# class Yazilimci(Calisan):
#     def __init__(self, isim, soyisim, maas,bildigi_dil):
#        super().__init__(isim,soyisim,maas)
#        self.bildigi_dil=bildigi_dil

#     def bilgileri_soyle(self):
#         return "Ad: {} Soyadı: {} Maaş: {} Email: {} Dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
#     def dilini_soyle(self):
#         return f"Bildiğim dil: {self.bildigi_dil}"

        
# yazilimci1=Yazilimci("Ayşe","Yıldız",7000,"Python")
# yazilimci2=Yazilimci("Fatma","Ay",8000,"Java")
# print(yazilimci1.dilini_soyle())