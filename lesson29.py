#str ve repr (Megic metodları)

#classtan oluşturduğunuz nesneleri nasıl stringe dönüştüreleceği

# a = "Python"
# print(str(a))
# print(repr(a))

# from datetime import date
# import datetime

# bugun = date.today
# print(bugun)
# print(str(bugun))
# print(repr(bugun))

# class Futbolcu:
#     def __init__(self,isim,soyisim,yas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.yas=yas
        
#     def __str__(self):
#         return f"Ad: {self.isim} Soyadı: {self.soyisim}"
    
#     def __repr__(self):
#         return "repr çalışıyor"

# futbolcu1=Futbolcu("Ali","Veli",20)
# print(futbolcu1)
# print(repr(futbolcu1))
# print(futbolcu1.__repr__)




# class Futbolcu:
#     def __init__(self,isim,soyisim,yas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.yas=yas
        
#     def __str__(self):
#         return f"Ad: {self.isim} Soyadı: {self.soyisim}"
    
#     def __repr__(self):
#         return f"Futbolcu: {self.isim}, {self.soyisim}, {self.yas}"

# futbolcu1=Futbolcu("Ali","Veli",20)
# print(futbolcu1)
# print(repr(futbolcu1))
# print(futbolcu1.__repr__)