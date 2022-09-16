# saving class
import sqlite3


class ReadFinances:
    """
    It connects to the database, selects all the rows from the finances table, and returns the rows
    :return: The rows of the finances table.
    """

    def getFinance(self, name):
        self.conn = sqlite3.connect("data.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM finances WHERE name = ?", (name,))
        self.rows = self.c.fetchall()
        self.c.close()
        self.conn.close()
        return self.rows
