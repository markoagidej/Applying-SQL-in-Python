 # 2. Advanced Data Analysis in Gym Management System

import mysql.connector
from mysql.connector import Error

def connect_db():
    # Connect to DB and return the connection
    try:
        conn = mysql.connector.connect(
            database="applying_sql_in_python",
            user="root",
            password="PASSWORD",
            host="localhost"
            )
        if conn.is_connected():
            return conn
    except Error as e:
        print("Problem connection to server.")
        print(f"Error: {e}")
        return None
    
def close_connection(connection, cursor):
    connection.close()
    cursor.close()

# Task 1: SQL DISTINCT Usage
def list_distinct_trainers():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            query = ("SELECT DISTINCT trainer_id FROM members")
            cursor.execute(query)
            results = cursor.fetchall()
            print("All trainer IDs:")
            for id in results:
                print(id[0])
        except Error as e:
            print("Error fetching trainer IDs.")
            print(f"Error: {e}")
        finally:
            close_connection(conn, cursor)

# Task 2: SQL COUNT Functionality


# Task 3: SQL BETWEEN Usage


# main
def main():
    list_distinct_trainers()

if __name__ == "__main__":
    main()