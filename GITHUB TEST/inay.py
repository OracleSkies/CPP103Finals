import mysql.connector
import hashlib

def create_database():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password321',
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS digitalInventoryLogDatabase")
    cursor.close()
    mydb.close()

def create_user_table():
    dbase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password321',
        database='digitalInventoryLogDatabase',
    )
    cursor = dbase.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS inventory_user (\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        user_name VARCHAR(255) UNIQUE, \
        user_password VARCHAR(255))"
    )
    cursor.close()
    dbase.close()

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def insert_user(username, password):
    """Insert a new user into the inventory_user table."""
    hashed_password = hash_password(password)
    dbase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password321',
        database='digitalInventoryLogDatabase',
    )
    cursor = dbase.cursor()
    try:
        cursor.execute('''
        INSERT INTO inventory_user (user_name, user_password) VALUES (%s, %s)
        ''', (username, hashed_password))
        dbase.commit()
        print(f"User {username} added successfully.")
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            print(f"Error: Username {username} already exists.")
        else:
            print(f"Error: {err}")
    finally:
        cursor.close()
        dbase.close()

# Example usage
if __name__ == "__main__":
    create_database()
    create_user_table()
    username = input("Enter username: ")
    password = input("Enter password: ")
