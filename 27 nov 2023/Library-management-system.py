class Library:
    def __init__(self,list,name):
        self.Booklist=list
        self.name=name
        self.leadlist={}

    def Display_Book(self):
        print(f"----IIIM College Books{self.name}------")
        for i in self.Booklist:
            print(i)
    def lend_Book(self,book,user):
        if book not  in self.leadlist.keys():
            self.leadlist.update({book:user})
            print("Lender-Book")
        else:
            print(f"Book is already being {self.leadlist[book]}")
    def Add_Book(self,book):
        self.Booklist.append(book)
        print("Book this added in Book library")

    def Return_Book(self,book):
        self.leadlist.pop(book)
if __name__ == '__main__':
    Library_Books=Library(['C','C++','Python','Java','CA','AI','Web Deveploment','SQL','OS'],"IIM")
    while(True):
        print("--------------Welcome to the IIIM College Books Library Details----------------")
        print(" 1. All Books Display \n 2. Lend a Book \n 3. Add a Book \n 4. Return a Book \n Ether:")
        choice=input()
        if choice not in ['1','2','3','4']:
            print("---------Plz Enter the valid Number-------")
            continue
        else:
            choice=int(choice)
        if choice == 1:
            Library_Books.Display_Book()
        elif choice == 2:
            book=input("Enter the Book name Lender:")
            name=input("Enter the Student name:")
            Library_Books.lend_Book(book,name)
        elif choice == 3:
            book=input("Ether the Book name: ")
            Library_Books.Add_Book(book)
        elif choice ==4:
            book=input("Eter the return book name")
            Library_Books.Return_Book(book)
        else:
            print("Invalied")