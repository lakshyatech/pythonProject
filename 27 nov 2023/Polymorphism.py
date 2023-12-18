# class Student:
#     def __init__(self):
#         self.name=input("Enter the name")
#     def data(self):
#         print("Sudent name",self.name)
# obj=Student()
# obj.data()

class Vehicle:
    def __init__(self,Car_Name):
        self.Car_Name=Car_Name
    def Move(self):
        print(f"Car is: {self.Car_Name}")

class Car(Vehicle):
    def __init__(self,Car_Name,Model):
        super().__init__(Car_Name)
        self.Model=Model
    def Move(self):
        print(f"Car Name: {self.Car_Name}"
              f"\n Car Model {self.Model}")
class Bicycle(Vehicle):
    def __init__(self,Car_Name,Car_Price):
        super().__init__(Car_Name)
        self.Car_Price=Car_Price
    def Move(self):
        print(f"Car Name is: {self.Car_Name}"
              f"\n Car Price {self.Car_Price}")

obj1=Vehicle("BMW")
print("-----Car Name----")
obj1.Move()
obj2=Car("Cody",2023)
print("-----Car Name and Model------")
obj2.Move()
obj3=Bicycle("ALTO 800","3.50 lakh")
print("-----Car Name and Car Price----------")
obj3.Move()
