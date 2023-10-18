#dunder methods (magic methods) double underscore

# print(3+5)
# print(int.__add__(3,5))
# print("Ali"+"Veli")
# print(str.__add__("Ali","Veli"))
# print([1,2,3]+[4,5,6])
# print(list.__add__([1,2,3],[4,5,6]))


# class Mylist(list):
#     pass
# liste1=Mylist([1,2,3])
# liste2=Mylist([4,5,6])

# print(liste1+liste2)


# class Mylist(list):
#     def __add__(self,other):
#         if len(self)!=len(other):
#             return "Bu elemanlar toplanamaz"
#         else: 
#             result = Mylist()
#             for i in range(len(self)):
#                 result.append(self[i]+other[i])
#         return result
#     def __sub__(self,other):
#         if len(self)!=len(other):
#             return "Bu elemanlar toplanamaz"
#         else: 
#             result = Mylist()
#             for i in range(len(self)):
#                 result.append(self[i]-other[i])
#         return result
        
#     def __eq__(self,other):
#         if sum(self) == sum(other):
#             return True
#         return False
#     def __abs__(self):
#         result = Mylist()
#         for i in self:
#             if i>=0:
#                 result.append(i)
#             else:
#                 result.append(-1*i)
#         return result
        

# liste1=Mylist([1,2,3])
# liste2=Mylist([-4,5,-6])

# print(liste1+liste2)
# print(liste1-liste2)
# print(liste1==liste2)
# print(abs(liste1))
# print(abs(liste2))


# class Futbolcu:
#     def __init__(self,isim,soyisim,yas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.yas=yas
#     def __eq__(self,other):
#         if self.isim==other.isim and self.soyisim==other.soyisim:
#             return True
#         return False
#     def __add__(self,other):
#         isim=self.isim[0]+other.isim[0]
#         soyisim=self.soyisim[0]+other.soyisim[0]
#         yas=self.yas+other.yas
#         return Futbolcu(isim,soyisim,yas)
#     def __lt__(self,other):
#         if self.yas<other.yas:
#             return True
#         return False
#     def __gt__(self,other):
#         if self.yas>other.yas:
#             return True
#         return False


# futbolcu1=Futbolcu("Ali","Veli",27)
# futbolcu2=Futbolcu("Hakan","Metin",30)
# futbolcu3=futbolcu1+futbolcu2


# print(futbolcu1==futbolcu2)
# print(futbolcu3.isim)
# print(futbolcu2>futbolcu1)

#Kendi classımızda kendi işlemlerimizi tanımlayabiliriz amacımız buydu.
