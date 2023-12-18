class Mahendra:
    def __init__(self,name,age,Address,Qualification):
        self.name=name
        self.age=age
        self.Address=Address
        self.Qualification=Qualification

    def Your_Name(self):
        return self.name
    def Your_age(self):
        return self.age
    def Your_DOB(self):
        return self.Address
    def Your_Qualification(self):
        return self.Qualification
print("-----Fill the your Details---")
n=input("Ether the Your Name:")
a=int(input("Enter the Your Age:"))
A=input("Enter the Your Address:")
q=input("Enter the Your Qualification:")
obj=Mahendra(n,a,A,q)
print()
print("---your Details---")
print("Your Name:",obj.Your_Name())
print("YOur Age:",obj.Your_age())
print("Your Address:",obj.Your_DOB())
print("YOur Qualification:",obj.Your_Qualification())
