class Finance():
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    
    def getBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount