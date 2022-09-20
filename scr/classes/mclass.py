import sqlite3



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



    def getFinance(self, name):
        self.conn = sqlite3.connect("data.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM finances WHERE name = ?", (name,))
        self.rows = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return self.rows




    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nBalance {self.balance}'