
def runCLI(store):
    """
    This is the main driver for the command line interface (CLI) based BookStore program. 
    It controls how the users inputs are processed.

    Parameters
    ----------
    store   : BookStore
        An instance of the BookStore class used for accessing the eBookStore database
    """
    opt = -1
    while opt != 0:
        # Show menu and get input
        opt = showMenu()
        
        # Process input
        if opt == 1:
            newEntry(store)
        elif opt == 2:
            updateEntry(store)
        elif opt == 3:
            deleteEntry(store) 
        elif opt == 4:
            searchEntries(store)
        elif opt == 5:
            print(store.listAllItems())
        elif opt == 6:
            deleteAll(store)
    return

def showMenu():
    """ The main menu for the program. Show the user the options for interacting with the program. """
    print("\nMain Menu")
    print(  "---------")
    print(" 1. Enter book")
    print(" 2. Update book")
    print(" 3. Delete book")
    print(" 4. Search book")
    print(" 5. List all books")
    print(" 6. Delete all books")
    print(" 0. Exit")
    try:
        opt = int(input("\nEnter option number: "))
    except:
        print("Invalid input! Please enter the number of the desired menu function. ")
    return opt

def newEntry(store):
    """
    Creates a new book entry in the eBookStore database
    
    Parameters
    ----------
    store   : BookStore
        An instance of the BookStore class used for accessing the eBookStore database
    """
    validEntry = False
    while validEntry == False:
        print("\nNew Entry:")
        print(  "----------")
        try:
            id   = int(input("ID:       "))
            name =     input("Name:     ")
            auth =     input("Author:   ")
            qty  = int(input("Quantity: "))
        except:
            print("Invalid Input")
        else:
            validEntry = True 
    store.addNewItem(id, name, auth, qty)
    print("Entry created successfully.")
    return

def updateEntry(store):
    """
    Update an existing book in the eBookStore database.

    Parameters
    ----------
    store   : BookStore
        An instance of the BookStore class used for accessing the eBookStore database
    """
    print("\nUpdate")
    print(  "------")
    change =  input("\nEnter what you would like to change (SQL format):  SET ")
    condition = input("Enter SQL search condition:                        WHERE ")
    try: 
        store.updateItem(change, condition)
    except:
        print("Invalid search condition. Please enter a valid SQL search condition.")
    else:
        print("Item successfully updated. ")
    return

def deleteEntry(store):
    """
    Remove an existing book from the eBookStore database.

    Parameters
    ----------
    store   : BookStore
        An instance of the BookStore class used for accessing the eBookStore database
    """
    print("\nDelete")
    print(  "------")
    condition = input("\nEnter SQL search condition:  WHERE ")
    try:
        print()
        print(store.removeItem(condition))
    except:
        print("Invalid search condition. Please enter a valid SQL search condition.")
    return

def searchEntries(store):
    """
    Search the eBookStore database.

    Parameters
    ----------
    store   : BookStore
        An instance of the BookStore class used for accessing the eBookStore database
    """
    print("\nSearch:")
    print(  "-------")
    condition = input("\nEnter SQL search condition:  WHERE ")
    try:
        print()
        print(store.searchItem(condition))
    except:
        print("Invalid search condition. Please enter a valid SQL search condition.")
    return

def deleteAll(store):
    """
    Removes all entries from the eBookStore database.

    Parameters
    ----------
    store   : BookStore
        An instance of the BookStore class used for accessing the eBookStore database
    """
    print("\nThis will remove all items from the eBookStore database.")
    yn = input("Are you sure you want to proceed? (y/n) ")
    if yn == "y":
        store.clearTable()
    elif yn != 'n':
        print("Invalid input, returning to main menu...")
    return