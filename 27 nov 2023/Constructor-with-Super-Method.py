class Company:
    def __init__(self,Cname,Caddress,Cwebsite):
        self.Cname=Cname
        self.Caddress=Caddress
        self.Cwebsite=Cwebsite
    def Show(self):
        print("Company Name:",self.Cname)
        print("Company address",self.Caddress)
        print("Company Website",self.Cwebsite)

class Employee(Company):
    def __init__(self,Cname,Caddress,Cwebsite,Ctotal_user,CusedL):
        super().__init__(Cname,Caddress,Cwebsite)
        self.Ctotal_user=Ctotal_user
        self.CusedL=CusedL
    def Show(self):
        super().Show()
        print("Company total User",self.Ctotal_user)
        print("Company Used Language",self.CusedL)


obj=Company("Etherenal Softech","jaipur","enterealsoftech.com")
obj1=Employee("Etherenal Softech","jaipur","enterealsoftech.com",50,"java,python,HTML/CSS,JavaScript")
print("-----------Ethereal Softech-------------")
obj.Show()
print()
print("-----------Used this Super() method Ethereal Softech-------------")

obj1.Show()
