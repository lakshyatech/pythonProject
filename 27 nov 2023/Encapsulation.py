# class mahendra:
#     _name="mahendra"   #Protected variable
#     __age=21    # Pravite variable
#     def show(self):
#         print(f"Your Name is {self._name} and Age {self.__age}")
# obj=mahendra()
# obj.show()
# print("outsite of class:",obj._name)        # Protected variable ko class ke bar used kr sk the hai

class BankAccount:
    def __init__(self,balance=0.0):
        self.__Balance=balance      # Pravite Variable

    def Deposit(self,amount):
        if amount >0:
            self.__Balance += amount
            print(f"Deposited ${amount} , New Balance {self.__Balance}")
        else:
            print("Invalid")
    def withdraw(self,amount):
        if 0<amount <=self.__Balance:
            self.__Balance-=amount
            print(f"Withdraw{amount} New Balance{self.__Balance}")
        else:
            print("Invalid Withdraw")
    def getBalance(self):
        return self.__Balance

obj=BankAccount(balance=1000.0)
obj.Deposit(700.0)
obj.withdraw(500.0)
obj.getBalance()
balance=obj.getBalance()
print(f"Current Balance {balance}")


