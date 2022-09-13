# saving class
import sqlite3

class SaveFinances:
    # saving class using sqlite3
    def __init__(self):
        # create a database
        self.db = 'data.db'
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS finances (name text, age integer, balance integer)''')
        self.conn.commit()
        self.c.close()
        self.conn.close()


    def save(self, finance):
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO finances VALUES (?, ?, ?)", (finance.getName(), finance.getAge(), finance.getBalance()))
        self.conn.commit()
        self.c.close()
        self.conn.close()