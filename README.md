# eBookStore-HyperionDev
A stock manager for an eBook store developed as the final task in the HyperionDev software engineering bootcamp. 


## About 
This was the final project task as part of the HyperionDev software engineering bootcamp, creating a stock managing application 
that utilises SQL via sqlite3 to manage the stored database. It is written in python and at present requires running in a terminal 
however, a linked GUI is in development using PyQt6.  

Requirements: 
* Python 3
* sqlite3 

## Running the Application 
The application downloaded and run from a command line as,

```
python main.py
``` 

This will present the user with the following menu, 

```
Main Menu
---------
 1. Enter book
 2. Update book
 3. Delete book
 4. Search book
 5. List all books
 6. Delete all books
 0. Exit
 ```

 where the user can input the number corresponding to the menu option they want to perform. 
 If no file database file, 'eBookStore.db' is present, one will be created and default values will be 
 added.
 
 All options require inputs in SQL format. For example, if option 2 (update book) is selected, 
 the user is presented with the following interface,
 
 ```
 Update
------

Enter what you would like to change (SQL format):  SET 
Enter SQL search condition:                        WHERE 
``` 

where the input lines require the user to input conditions after the SET and WHERE statements in SQL 
format. An example of which would look like,

```
Update
------

Enter what you would like to change (SQL format):  SET title='New title'
Enter SQL search condition:                        WHERE id=3007
```

where the title for the book with the id=3007 is being changed to 'New title'. 

The outputs from this program are formatted as a table as follows, 

```
ID      Title                                         Author          Qty
------  --------------------------------------------- --------------- ----
  3001  A Tale of Three Cities                        Charles Dickens   30
  3002  Harry Potter and the Philosopher's Stone      J.K Rowling       40
  3003  The Lion the Witch and the Wardrobe           C.S Lewis         25
  3004  The Lord of The Rings                         J.R.R Tolkien     37
  3005  Alice in Wonderland                           Lewis Carroll     12
```

## Credits 
This project was developed by Dr. Benjamin T. Speake for the HyperionDev software engineering bootcamp.
