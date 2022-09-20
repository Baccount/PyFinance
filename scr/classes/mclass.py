import sqlite3



class Finance():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.db = "data.db"
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS finances (name text, balance integer)"""
        )
        self.conn.commit()
        self.c.close()
        self.conn.close()

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


    def save(self, finance):
        # Saving the data into the database.
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        # check if the name is already in the database
        self.c.execute("UPDATE finances SET balance = balance + ? WHERE name = ?", (finance.getBalance(), finance.getName().lower()))
        self.c.execute("INSERT INTO finances (name, balance) SELECT ?, ? WHERE (SELECT Changes() = 0)", (finance.getName(), finance.getBalance()))
        self.conn.commit()
        self.c.close()
        self.conn.close()




    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nBalance {self.balance}'