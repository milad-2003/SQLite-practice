import sqlite3

try:
    # Connecting the database and creating a cursor object
    connection = sqlite3.connect("database.db")
    print("[+] Connected to the database...")

    # Creating a cursor object of the connection
    cursor = connection.cursor()

    # Executing queries on the database
    query = "select sqlite_version();"
    cursor.execute(query)

    # Fetch and output result
    result = cursor.fetchall()
    print(f"The currunt version of sqlite is {result}")

    # Dropping the table if it already exists,
    # to prevent error: "table users already exists"
    cursor.execute("DROP TABLE IF EXISTS users")

    # Creating a table named users with 4 columns
    cursor.execute("""CREATE TABLE users (
                   Name TEXT,
                   Age INTEGER,
                   Credit REAL,
                   Email TEXT
                   );""")

    # Closing the cursor when we are done with it
    cursor.close()
    
except connection.Error as error:
    # Printing an error message for the user in case there is one
    print(f"Error occured - {error}")

finally:
    # Closing the connection whether we had an error or not
    if connection:
        connection.close()
        print("[+] Connection has been closed")
