#Sınıf ve Örnek kavramları (class and instance)
#class oluşturma
#Özellik ve metotlar(attributes and methods)


#class nasıl oluşturulur ve örnek nasıl elde edilir örneği

# class calisan:
#     pass
# calisan1=calisan()
# calisan1.name="Ali"
# calisan1.surname="Veli"
# calisan1.age=20
# print(calisan1.name)
# print(calisan1.surname)


# class calisan:
#     def __init__(self,name,surname,age):
#         print(" __init__ fonksiyonu çalışıyor")
#         self.name=name
#         self.surname=surname
#         self.age=age

# calisan1=calisan("Ali","Veli",20)
# print(calisan1.name,calisan1.surname,calisan1.age)

# calisan2=calisan("Ahmet","Mehmet",25)
# print(calisan2.name,calisan2.surname,calisan2.age)





#bir classa bağlı fonksiyonlara metot denir

# class calisan:
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#     def show_info(self):
#         print(f"Ad: {self.name},Soyadı: {self.surname}, Yaş: {self.age}")
# calisan1=calisan("Ali","Veli",20)
# print(calisan1.name,calisan1.surname,calisan1.age)

# calisan2=calisan("Ahmet","Mehmet",25)
# print(calisan2.name,calisan2.surname,calisan2.age)

# calisan1.show_info()
# calisan2.show_info()



# class calisan:
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#     def show_info(self):
#         print(f"Ad: {self.name},Soyadı: {self.surname}, Yaş: {self.age}")
# calisan1=calisan("Ali","Veli",20)


# calisan2=calisan("Ahmet","Mehmet",25)


# calisan.show_info(calisan1)
# calisan.show_info(calisan2)

