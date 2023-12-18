class Student:
    def __init__(self,Student_id,Student_name,Student_Branch,Student_Address):
        self.Student_id=Student_id
        self.Student_name=Student_name
        self.Student_Brach=Student_Branch
        self.Student_Address=Student_Address
    def Student_Add(self,S_ID,S_Name,S_Branch,S_A):
        ob=Student(S_ID,S_Name,S_Branch,S_A)
        ls.append(ob)
    def Student_Details(self,ob):
        print(f"Student ID: {ob.Student_id} \n"
              f"Student Name: {ob.Student_name} \n"
              f"Student Branch Name: {ob.Student_Brach} \n"
              f"Student Address: {ob.Student_Address}")
        print()
    def Student_Search(self,StudentID):
        for i in range(ls.__len__()):
            if ls[i].Student_id == StudentID:
                return i
    def Student_Delete(self,StudentID):
        i=obj.Student_Search(StudentID)
        del ls[i]
    def Student_Update(self,StudentID,Number):
        i=obj.Student_Search(StudentID)
        ID= Number
        ls[i].Student_id = ID
ls =[]
obj=Student(0,'','','')
while(True):
    print(" 1. Student Add \n 2. Student Details \n 3.Student Search \n 4. Student Delete \n 5 Student Details Update \n 6. Exit")
    choice=int(input("Enter the choice:"))
    if choice ==1:
        obj.Student_Add(101,'mahendra sain','MCA','Jaipur')
        obj.Student_Add(102,'Nihit','MCA','Jaipur')
        obj.Student_Add(103,'gagan','MCA','Jaipur')
    elif choice ==2:
        print("Student of List ")
        for i in range(ls.__len__()):
            obj.Student_Details(ls[i])
    elif choice ==3:
        print("Student search ")
        s=obj.Student_Search(2)
        obj.Student_Details(ls[s])
    elif choice ==4:
        obj.Student_Delete(2)
        print(ls.__len__())
        print("list cafter delete")
        for i in range(ls.__len__()):
            obj.Student_Details(ls[i])
    elif choice == 5:
        obj.Student_Update(3,2)
        print("list after Update ")
        for i in range(ls.__len__()):
            obj.Student_Update(ls[i])
    else:
        print("Invalid Value")



