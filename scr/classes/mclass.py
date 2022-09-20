import sqlite3



class Finance():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.createDB()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def getSaved(self, name): 
        self.conn = sqlite3.connect("data.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM finances WHERE name = ?", (name,))
        self.rows = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return self.rows


    def saveFinance(self):
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        # check if the name is already in the database
        self.c.execute("UPDATE finances SET balance = balance + ? WHERE name = ?", (self.getBalance(), self.getName().lower()))
        self.c.execute("INSERT INTO finances (name, balance) SELECT ?, ? WHERE (SELECT Changes() = 0)", (self.getName(), self.getBalance()))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def createDB(self):
        self.db = "data.db"
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS finances (name text, balance integer)"""
        )
        self.conn.commit()
        self.c.close()
        self.conn.close()


    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nBalance {self.balance}'