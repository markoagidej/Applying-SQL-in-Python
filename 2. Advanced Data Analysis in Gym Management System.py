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
        # Try to slect and print as list of trainer IDs 
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
def count_members_per_trainer():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # Try to find count of memebers per trainer_id then print results
        try:
            query = ("SELECT trainer_id, COUNT(*) as member_count FROM members GROUP BY trainer_id")
            cursor.execute(query)
            results = cursor.fetchall()
            print("List of number of members assigned per trainer ID:")
            for result in results:
                print(f"{result[0]}: {result[1]}")
        except Error as e:
            print("Error fetching member count per trainer.")
            print(f"Error: {e}")
        finally:
            close_connection(conn, cursor)

# Task 3: SQL BETWEEN Usage
def get_members_in_age_range(start_age, end_age):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # Try to find age of memebers between the start and end age
        try:
            age_values = (start_age, end_age)
            query = ("SELECT name, age FROM members WHERE age BETWEEN %s and %s")
            cursor.execute(query, age_values)
            results = cursor.fetchall()
            if results:
                print(f"List of members between ages {start_age} and {end_age}:")
                for result in results:
                    print(f"{result[0]}: {result[1]}")
            else:
                print(f"No members between ages {start_age} and {end_age}!")
        except Error as e:
            print("Error fetching members between specified ages.")
            print(f"Error: {e}")
        finally:
            close_connection(conn, cursor)


# main
def main():
    list_distinct_trainers()
    count_members_per_trainer()
    start = input("Enter a start age: ")
    end = input("Enter an end age: ")
    get_members_in_age_range(start, end)

if __name__ == "__main__":
    main()