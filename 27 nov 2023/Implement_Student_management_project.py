class Student:
    def __init__(self,Student_id,Student_name,Student_Branch,Student_Address):
        self.Student_id=Student_id
        self.Student_name=Student_name
        self.Student_Brach=Student_Branch
        self.Student_Address=Student_Address
    def Student_ID(self):
        return self.Student_id
    def Student_Name(self):
        return self.Student_name
    def Student_Branch(self):
        return self.Student_Brach
    def Student_Address(self):
        return self.Student_Address
# ls =[]
# obj=Student(0,'','','')
# while(True):
#     print(" 1. Student Add \n 2. Student Details \n 3.Student Search \n 4. Student Delete \n 5 Student Details Update \n 6. Exit")
#     choice=int(input("Enter the choice:"))
#     if choice ==1:
#         obj.Student_Add(101,'mahendra sain','MCA','Jaipur')
#         obj.Student_Add(102,'Nihit','MCA','Jaipur')
#         obj.Student_Add(103,'gagan','MCA','Jaipur')
#     elif choice ==2:
#         print("Student of List ")
#         for i in range(ls.__len__()):
#             obj.Student_Details(ls[i])
#     elif choice ==3:
#         print("Student search ")
#         s=obj.Student_Search(2)
#         obj.Student_Details(ls[s])
#     elif choice ==4:
#         obj.Student_Delete(2)
#         print(ls.__len__())
#         print("list cafter delete")
#         for i in range(ls.__len__()):
#             obj.Student_Details(ls[i])
#     elif choice == 5:
#         obj.Student_Update(3,2)
#         print("list after Update ")
#         for i in range(ls.__len__()):
#             obj.Student_Update(ls[i])
#     else:
#         print("Invalid Value")



class College:
    def __init__(self):
        self.n=[]
        self.member=[]
    def add(self,name):
        self.n.append(name)

    def remove_book(self,name):
        if name in self.n:
            self.n.remove(name)
    def display(self):
        for i in self.n:
            print(f"Student ID: {i.Student_ID()}, "
                  f" And Student Name: {i.Student_Name()}, "
                  f"Student Branch Name: {i.Student_Branch()},  "
                  f"Student Address:{i.Student_Address} ")
l= College()
n1 = Student(101, "Mahendra Sain", "MCA","Jaipur")
n2 = Student(102,"Nihit","MCA","Jaipur")
print("-----IIIM College Student Add Name-----")
l.add(n1)
l.display()
print()
l.add(n2)
print("----IIIM College All Student Add list---")

# l.remove_book(n1)
l.display()
