

def runCLI(store):
    opt = -1
    while opt != 0:
        # Show menu and get input
        opt = showMenu()
        
        # Process input
        if opt == 1:
            pass
        elif opt == 2:
            pass
        elif opt == 3:
            pass 
        elif opt == 4:
            pass
        elif opt == 5:
            print(store.listAllItems())




def showMenu():
    print("\nMain Menu")
    print(  "---------")
    print(" 1. Enter book")
    print(" 2. Update book")
    print(" 3. Delete book")
    print(" 4. Search book")
    print(" 5. List all books")
    print(" 0. Exit")
    try:
        opt = int(input("\nEnter option number: "))
    except:
        print("Invalid input! Please enter the number of the desired menu function. ")
    return opt