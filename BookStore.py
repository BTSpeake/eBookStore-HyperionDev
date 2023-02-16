import sqlite3
from CLI import runCLI 
# from GUI import runGUI

class BookStore:

    tableTitle = "{0:6s}  {1:45s} {2:15s} {3:4s}\n".format("ID", "Title", "Author", "Qty")
    tableSeparator = "{0:6s}  {1:45s} {2:15s} {3:4s}\n".format("-"*6, "-"*45, "-"*15, "-"*4)
    rowStr = "{0:6d}  {1:45s} {2:15s} {3:4d}\n"

    def __init__(self):
        self.db = sqlite3.connect("eBookStore.db")
        self.cursor = self.db.cursor()
        return 

    def listAllItems(self):
        print("")
        self.cursor.execute('''
                            SELECT * FROM Books
                            ''')
        return self.getTableString()

    def getTableString(self):
        oStr = BookStore.tableTitle
        oStr += BookStore.tableSeparator
        for row in self.cursor:
            oStr += BookStore.rowStr.format(row[0], row[1], row[2], row[3])
        return oStr
    
    def addNewItem(self, id : int, title : str, author : str, qty : int):
        print("")
        self.cursor.execute('''
                            INSERT INTO Books 
                                VALUES (?, ?, ?, ?)''',
                                (id, title, author, qty))
        self.db.commit()
        return 

    def updateItem(self, change : str, condition : str):
        self.cursor.execute('''
                            UPDATE Books
                            SET {0}
                            WHERE {1} ;'''.format(change, condition)
                            )
        self.db.commit()
        return

    def removeItem(self, condition : str):
        self.cursor.execute('''
                            DELETE FROM Books
                            WHERE {0};'''.format(condition)
                            )
        self.db.commit()
        return

    def searchItem(self, condition : str):
        self.cursor.execute('''
                            SELECT * FROM Books
                            WHERE {0};'''.format(condition)
                            )
        return self.getTableString()

    def clearTable(self):
        self.cursor.execute('DELETE FROM Books')
        self.db.commit()
        return

