import sqlite3

try:
    # Connecting the database and creating a cursor object
    connection = sqlite3.connect("database.db")

    # Creating a cursor object of the connection
    cursor = connection.cursor()

    # Some code here to modify the database using the cursor...
    # Some code here to modify the database using the cursor...
    # Some code here to modify the database using the cursor...

    # Closing the cursor when we are done with it
    cursor.close()
    
except connection.Error as error:
    # Printing an error message for the user in case there is one
    print(f"Error occured - {error}")
