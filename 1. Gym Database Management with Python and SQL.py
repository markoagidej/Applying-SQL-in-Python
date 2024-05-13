# 1. Gym Database Management with Python and SQL

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

# Task 1: Add a Member
def add_member(name, age, trainer_id): # no "id" included because the database will handle auto incrementing a unique id for members
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            member_info = (name, age, trainer_id)
            query = "INSERT INTO members (name, age, trainer_id) VALUES (%s, %s, %s)"
            cursor.execute(query, member_info)
            conn.commit()
            print(f"New member {name} added!")
        except Error as e:
            print("Problem adding member.")
            print(f"Error: {e}")
        finally:
            close_connection(conn, cursor)

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration, calories_burned):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # First try to see if there is a member with the requested member_id
        try:
            memeber_id_value = (member_id,)
            search_query = "SELECT * FROM members WHERE id = (%s)"
            cursor.execute(search_query, memeber_id_value)
            if not cursor.fetchone():
                print(f"There was no member found with id of \'{member_id}\'!")
                close_connection(conn, cursor)
                return
        except Error as e:
            print("Problem searching for member.")
            print(f"Error: {e}")
            close_connection(conn, cursor)
            return
        # Try to insert the new workout session
        try:
            workout_info = (member_id, date, duration, calories_burned)
            query = "INSERT INTO workout_sessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, workout_info)
            conn.commit()
            print(f"New workout added for member: {member_id} added!")
        except Error as e:
            print("Problem adding a workout session.")
            print(f"Error: {e}")
        finally:
            close_connection(conn, cursor)

# Task 3: Updating Member Information
def update_member_age(member_id, age):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # First try to see if there is a member with the requested member_id
        try:
            memeber_id_value = (member_id,)
            search_query = "SELECT * FROM members WHERE id = (%s)"
            cursor.execute(search_query, memeber_id_value)
            if not cursor.fetchone():
                print(f"There was no member found with id of \'{member_id}\'!")
                close_connection(conn, cursor)
                return
        except Error as e:
            print("Problem searching for member.")
            print(f"Error: {e}")
            close_connection(conn, cursor)
            return
        # Try to update the age of requested member
        try:
            update_info = (age, member_id)
            query = "UPDATE members SET age = %s WHERE id = %s"
            cursor.execute(query, update_info)
            conn.commit()
            print(f"Age of member number \'{member_id}\' updated to {age}!")
        except Error as e:
            print("Problem updating member's age.")
            print(f"Error: {e}")
            close_connection(conn, cursor)
            return
        finally:
            close_connection(conn, cursor)

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # First try to see if there is a session with the requested session_id
        try:
            session_value = (session_id,)
            search_query = "SELECT * FROM workout_sessions WHERE id = (%s)"
            cursor.execute(search_query, session_value)
            if not cursor.fetchone():
                print(f"There was workout session found with id of \'{session_id}\'!")
                close_connection(conn, cursor)
                return
        except Error as e:
            print("Problem searching for session.")
            print(f"Error: {e}")
            close_connection(conn, cursor)
            return
        # Try to delete teh session by session_id
        try:
            query = "DELETE FROM workout_sessions WHERE id = (%s)"
            cursor.execute(query, session_value)
            conn.commit()
            print(f"Workout Session \'{session_id}\' deleted!")
        finally:
            close_connection(conn, cursor)

# Main
def main():
    while True:
        print("Menu:")
        print("1. Add Member")
        print("2. Add Workout Session")
        print("3. Update Member Age")
        print("4. Delete a Workout Session")
        print("5. Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Only enter a number 1-5")
            continue

        if choice == 1: # Add Member
            name = input("What is the new member name: ")
            age = input(f"What is {name}'s age: ")
            trainer_id = input(f"What is the id of {name}'s trainer: ") # No trainer table explicit in problem, so just accepting any int here
            add_member(name, age, trainer_id)
        elif choice == 2: # Add Workout
            member_id = input("Enter the Member id of the workout: ")
            date = input("Enter the date of the workout: ")
            duration = input("Enter the duration in minutes of the workout: ")
            calories_burned = input("Enter the amount of calories burned for the workout: ")
            add_workout_session(member_id, date, duration, calories_burned)
        elif choice == 3: # Update Member Age
            member_id = input("Enter the Member id to update the age of: ")
            age = input("Enter the corrected age for this member: ")
            update_member_age(member_id, age)
        elif choice == 4: # Delete Workout Session
            session_id = input("What is the id of the session you wish to delete: ")
            delete_workout_session(session_id)
        elif choice == 5:
            print("Thank you, goodbye!")
            exit()


if __name__ == "__main__":
    main()