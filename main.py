class Bank:
    def __init__(self,bal,acc) :
        self.balance=int(bal)
        self.account_no=acc
        # self.__password=pas
        print(f"your current balance is {bal}")
    def deposit(self,amt):
        self.balance+=amt
        print(f"your  deposited money is {amt} and current balance is {self.blnce()}")
    def Credit(self,credit):
        self.balance-=credit
        print(f"your credit money amount is {credit} and current balance is {self.blnce()}")
    def blnce(self):
        return self.balance
    # def get_password(self):

    #     return self.__password
        


# money=Bank(1000,"sikandar")
# money.deposit(2000)
# money.Credit(1000)
class Thebank(Bank):
    def __init__(self, bal, acc,name ):
        self.name=name
        super().__init__(bal, acc)
        while True:
         transection=(input("want to do transection if yes press Y  otherwise N/n")).upper()
         if transection=="Y":
            type=(input("For deposit press 'D' for credit 'C'\n")).upper()
            if type=='D':
                self.deposit(int(input("enter money deposited here\n")))
            if type=='C':
                self.Credit(int(input("enter money want to credit here\n")))
         if transection=='N':
            print(f"your current balance is {self.balance}")
            break #this will turn true to false and again transection will not be asked
                 
        
        # money=Bank(int(input("enter your current balance here")),input("enter branch name here\n"))
        # money.deposit(int(input("enter money deposited here\n")))
        # money.Credit(int(input("enter enter credit money  here\n")))
        print(f"Mr. {self.name} your  {self.account_no} bank account has current balance of {self.balance} ")

# money=Bank(int(input("enter your current balance here")),input("enter branch name here\n"))
# money.deposit(int(input("enter money deposited here\n")))
# money.Credit(int(input("enter enter credit money  here\n")))
# lite=Bank(20,32,23)
# print(lite.get_password()) #these 49 and 50 code of lines are the one which encaptulates the private attribute of one  class using a method then calling that method
bank=Thebank(input("enter balance here\n"),input("enter branch name here\n"),input("enter user name here\n"))