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
    
    # Inserting values into the table
    cursor.execute("""INSERT INTO users VALUES
                   ("Milad", 21, 1500.0, "miladvalizadeh2003@gmail.com");
    """)

    # Inserting values into the table in a different order
    cursor.execute("""INSERT INTO users (Name, Credit, Email, Age) VALUES
                   ("Amin", 1000.0, "amin@gmail.com", 19);
""")
    
    # Inserting many values at the same time into the table
    many_users = [
        ("Alireza", 22, 2000.0, "alireza@gmail.com"),
        ("Mahdi", 20, 500.0, "mahdi@gmail.com"),
        ("Hosein", 19, 2500.0, "hosein@gmail.com")
    ]
    cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", many_users)

    # Printing all the items
    print("\nAll the items:")
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print("Name\tAge\tCredit\tEmail")
    print("----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}")

    # Printing all the items with their row id
    print("\nAll the items with their row id:")
    cursor.execute("SELECT rowid, * FROM users")
    data = cursor.fetchall()
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    # Printing some of the items with their row id (In this case: First 3 rows)
    print("\nSome of the items with their row id:")
    cursor.execute("SELECT rowid, * FROM users")
    data = cursor.fetchmany(3)
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    # Printing one item without its row id (First row)
    print("\nOne item without its row id:")
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchone()
    print("Name\tAge\tCredit\tEmail")
    print("----\t---\t------\t-----")
    print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}")

    # Selecting and printing items with a condition using WHERE Clause
    print("\nItems with an age greater than 20:")
    cursor.execute("SELECT rowid, * FROM users WHERE Age > 20")
    data = cursor.fetchall()
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    # Selecting and printing items that their name starts with "M"
    print("\nItems that their name starts with 'M':")
    cursor.execute("SELECT rowid, * FROM users WHERE Name LIKE 'M%'")
    data = cursor.fetchall()
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    # Updating the database
    print("\nUpdating the data of the second row and printing the table")
    cursor.execute("UPDATE users SET Age = 40 WHERE rowid = 2")
    data = cursor.execute("SELECT rowid, * FROM users").fetchall()
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    # Sorting the rows
    print("\nSorting the rows in the Ages order, descending:")
    cursor.execute("SELECT rowid, * FROM users ORDER BY Age DESC")
    data = cursor.fetchall()
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    print("\nSorting the rows in the Ages order, ascending:")
    cursor.execute("SELECT rowid, * FROM users ORDER BY Age ASC")
    data = cursor.fetchall()
    print("ID\tName\tAge\tCredit\tEmail")
    print("--\t----\t---\t------\t-----")
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

    # Commit the changes to the database
    connection.commit()

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
