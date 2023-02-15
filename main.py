import os
from BookStore import BookStore
from CLI import runCLI 
from GUI import runGUI

def main():
    if os.path.isfile("eBookStore.db"):
        store = BookStore()
    else:
        store = createFirstInstance()
    # runGUI(store)
    runCLI(store)
    store.db.close()
    return


def createFirstInstance():
    """
    If this is the first time the program has been run, the new data base file is 
    created and the Books table is populated with the default values from the task 
    description.

    Returns
    -------
    store   : BookStore 
        A class containing the data base instance and functions to interact with it. 
    """
    print("Creating the data base file...")
    try:
        store = BookStore()
        store.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Books (
                            id int(4) NOT NULL, 
                            title varchar(64),
                            author varchar(32),
                            qty int(3),
                            PRIMARY KEY (id)
                        )
                        ''')
        store.db.commit()
    except Exception as e:
        store.db.close()
        raise e

    # Enter default values from task 
    store.addNewItem(id=3001, title="A Tale of Two Cities", author="Charles Dickens", qty=30)
    store.addNewItem(id=3002, title="Harry Potter and the Philosopher's Stone", author="J.K Rowling", qty=40)
    store.addNewItem(id=3003, title="The Lion the Witch and the Wardrobe", author="C.S Lewis", qty=25)
    store.addNewItem(id=3004, title="The Lord of The Rings", author="J.R.R Tolkien", qty=37)
    store.addNewItem(id=3005, title="Alice in Wonderland", author="Lewis Carroll", qty=12)
    return store 




if __name__ == "__main__":
    main()