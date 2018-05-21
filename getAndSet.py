class CreditAccount:

    def __init__(self, balance):
        self.balance = balance
        self.transaction = []

    def removeFunds(self, funds):
        self.funds = funds
        self.balance = self.balance - self.funds
        self.transaction.append("#DF56178")

    def increaseFunds(self, funds):
        self.balance = self.balance + funds
        self.transaction.append("#IF75893")

class SavingsAccount:
    
    def __init__(self, balance):
        self.balance = balance
        self.transaction = []

    def removeFunds(self, funds):
        if funds > 20:
            return 0
        else:
            self.balance = self.balance - funds

"Getters and Setters for CreditAccount class"
#Creating variable to plug into class functions
bal = 100
fundOut = 30
fundIn = 10
#Initiating instance of CreditAccount class
caccount = CreditAccount(bal)
#Printing balance
print(caccount.balance)
#Calling on removeFunds function and setting funds variable
caccount.removeFunds(fundOut)
#Printing balance variable
print(caccount.balance)
#Calling on increaseFunds function and setting new instance variable funds
caccount.increaseFunds(fundIn)
print(caccount.balance)
print(caccount.transaction)

"Getters and Setters for SavingsAccount class"
#Initiating instance of SavingsAccount class
saccount = SavingsAccount(bal)
print(saccount.balance)
saccount.removeFunds(17)
print(saccount.balance)
