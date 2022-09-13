class Finance():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name


    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nBalance {self.balance}'