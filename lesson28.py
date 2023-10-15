##inheritance kalıtım2

# class Calisan:
     
#      def __init__(self,isim,soyisim,maas):
#          self.isim=isim
#          self.soyisim=soyisim
#          self.maas=maas
#          self.email=isim + soyisim + "@sirket.com"
#      def bilgileri_soyle(self):
#          return "Ad: {} Soyadı: {} Maaş: {} Email: {}".format(self.isim,self.soyisim,self.maas,self.email)

# calisan1=Calisan("Ali","Çalışkan",5000)
# calisan2=Calisan("Veli","Uzun",6000)

# class Yazilimci(Calisan):
#      def __init__(self, isim, soyisim, maas,bildigi_dil):
#         super().__init__(isim,soyisim,maas)
#         self.bildigi_dil=bildigi_dil

#      def bilgileri_soyle(self):
#          return "Ad: {} Soyadı: {} Maaş: {} Email: {} Dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
#      def dilini_soyle(self):
#          return f"Bildiğim dil: {self.bildigi_dil}"

# class Yönetici(Calisan):
 
#     def __init__(self, isim, soyisim, maas,calisanlar=None):
#      super().__init__(isim,soyisim,maas)
#      if calisanlar == None:
#        self.calisanlar =[]
#      else:
#        self.calisanlar=calisanlar

#     def calisan_ekle(self,Calisan):
#         if Calisan not in self.calisanlar:
#             self.calisanlar.append(Calisan)
#     def calisan_sil(self,Calisan):
#         if Calisan in self.calisanlar:
#             self.calisanlar.remove(Calisan)
#     def calisanlari_göster(self):
#      for Calisan in self.calisanlar:
#         print(Calisan.bilgileri_soyle())


# yazilimci1=Yazilimci("Ayşe","Yıldız",7000,"Python")
# yazilimci2=Yazilimci("Fatma","Ay",8000,"Java")

# yonetici1=Yönetici("Metin","Ali",10000)
# yonetici1.calisan_ekle(calisan1)
# yonetici1.calisan_ekle(yazilimci1)

# yonetici1.calisanlari_göster()
# print("**********")
# yonetici1.calisan_sil(calisan1)
# yonetici1.calisanlari_göster()
# yonetici2= Yönetici("Deniz","Güney",9000,[yazilimci1,yazilimci2,calisan1])
# yonetici2.calisanlari_göster()


# print(isinstance(yonetici2,Calisan))
# print(issubclass(Yazilimci,Calisan))
    
        
