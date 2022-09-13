class Finance():
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


    def getBalance(self):
        return self.balance

    def getAge(self):
        return self.age

    def getName(self):
        return self.name


    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nBalance {self.balance}'