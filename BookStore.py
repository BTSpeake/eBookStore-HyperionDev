import sqlite3
from CLI import runCLI 
# from GUI import runGUI

class BookStore:
    """
    A class for controlling interactions with the eBookStore.db database file.
    """

    tableTitle = "{0:6s}  {1:45s} {2:15s} {3:4s}\n".format("ID", "Title", "Author", "Qty")
    tableSeparator = "{0:6s}  {1:45s} {2:15s} {3:4s}\n".format("-"*6, "-"*45, "-"*15, "-"*4)
    rowStr = "{0:6d}  {1:45s} {2:15s} {3:4d}\n"

    def __init__(self):
        """ Initialises the connection to the database file. """
        
        self.db = sqlite3.connect("eBookStore.db")
        self.cursor = self.db.cursor()
        return 

    def listAllItems(self):
        """
        Lists all rows stored in the database under the Books table. The return links the 
        the BookStore.getTableString() function which will return the relevant formatted 
        table of data from the most recently executed SQL instruction. 
        """
        
        print("")
        self.cursor.execute('''
                            SELECT * FROM Books
                            ''')
        return self.getTableString()

    def getTableString(self):
        """
        Returns the relevant formatted table of data from the most recently executed SQL 
        instruction. 

        Returns
        -------
        oStr    : string 
            The formatted data from the SQL cursor object. 
        """

        oStr = BookStore.tableTitle
        oStr += BookStore.tableSeparator
        for row in self.cursor:
            oStr += BookStore.rowStr.format(row[0], row[1], row[2], row[3])
        return oStr
    
    def addNewItem(self, id : int, title : str, author : str, qty : int):
        """ 
        Adds a new item (row) to the database. 
        
        Parameters
        ----------
        id      : int 
            The ID value for the new item 
        title   : string 
            The title value for the new item 
        author  : string 
            The author value for the new item 
        qty     : int 
            The quantity value for the new item
        """

        print("")
        self.cursor.execute('''
                            INSERT INTO Books 
                                VALUES (?, ?, ?, ?)''',
                                (id, title, author, qty))
        self.db.commit()
        return 

    def updateItem(self, change : str, condition : str):
        """
        Updates an item within the database according to a SQL formatted SET and
        WHERE statements. 

        Parameters
        ----------
        change  : string 
            The SQL formatted SET statement for the update command
        condition: string 
            The SQL formatted WHERE statement for the update command
        """

        self.cursor.execute('''
                            UPDATE Books
                            SET {0}
                            WHERE {1} ;'''.format(change, condition)
                            )
        self.db.commit()
        return

    def removeItem(self, condition : str):
        """
        Removes an item from within the database according to a SQL formatted 
        WHERE statement. 

        Parameters
        ----------
        condition: string 
            The SQL formatted WHERE statement for the update command
        """

        self.cursor.execute('''
                            DELETE FROM Books
                            WHERE {0};'''.format(condition)
                            )
        self.db.commit()
        return

    def searchItem(self, condition : str):
        """
        Searches an item(s) from within the database according to a SQL formatted 
        WHERE statement. 

        Parameters
        ----------
        condition: string 
            The SQL formatted WHERE statement for the update command
        """

        self.cursor.execute('''
                            SELECT * FROM Books
                            WHERE {0};'''.format(condition)
                            )
        return self.getTableString()

    def clearTable(self):
        """ Deletes all items from within the database Books table. """
        
        self.cursor.execute('DELETE FROM Books')
        self.db.commit()
        return

