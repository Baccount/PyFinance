# saving class
import sqlite3


class SaveFinances:
    # saving class using sqlite3
    def __init__(self):
        """
        It saves the data into the database.

        :param finance: The finance object that we want to save to the database
        """
        self.db = "data.db"
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS finances (name text, balance integer)"""
        )
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def save(self, finance, amount):
        # Saving the data into the database.
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()
        # check if the name is already in the database
        self.c.execute("UPDATE finances SET balance = balance + ? WHERE name = ?", (finance.getBalance() + amount, finance.getName().lower()))
        self.c.execute("INSERT INTO finances (name, balance) SELECT ?, ? WHERE (SELECT Changes() = 0)", (finance.getName(), finance.getBalance() + amount))
        self.conn.commit()
        self.c.close()
        self.conn.close()
