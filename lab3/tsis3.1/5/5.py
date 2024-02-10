class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money
        if(self.balance < 0):
            print("You dont have enough money")
        else:
            print(self.balance)

wallet = Account("Sasha", 100000)
wallet.deposit(50000)
wallet.withdraw(150000)