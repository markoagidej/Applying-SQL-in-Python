# 1. Gym Database Management with Python and SQL

import mysql.connector
from mysql.connector import Error

def connect_db():
    # Connect to DB and return the connection
    try:
        conn = mysql.connector.connect("applying_sql_in_python", "root", "*963.MADEupPASSWORD", "localhost")
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Task 1: Add a Member
def add_member(name, age, trainer_id): # no "id" included because the database will handle auto incrementing a unique id for Members
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            member_info = (name, age, trainer_id)
            query = "INSERT INTO Members (name, age, trainer_id) VALUES (%s, %s, %s)"
            cursor.execute(query, member_info)
            conn.commit()
            print(f"New member {name} added!")
        finally:
            cursor.close()
            conn.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration, calories_burned):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            workout_info = (member_id, date, duration, calories_burned)
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, workout_info)
            conn.commit()
            print(f"New workout added for member: {member_id} added!")
        finally:
            cursor.close()
            conn.close()

# Task 3: Updating Member Information
def update_member_age(member_id, age):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # First try to see if there is a member with the requested member_id
        try:
            age_value = (age)
            search_query = "SELECT * FROM Members WHERE age = (%s)"
            cursor.execute(search_query, age_value)
            if cursor.fetchone():
                print(f"There was no member found with id of \'{member_id}\'!")
                return
        except:
            print("Problem searching for member")
            cursor.close()
            conn.close()
            return
        # Try to update the age of requested member
        try:
            update_info = (member_id, age)
            query = "UPDATE Members VALUES (%s, %s, %s, %s)"
            cursor.execute(query, update_info)
            conn.commit()
            print(f"New workout added for member: {member_id} added!")
        finally:
            cursor.close()
            conn.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        # First try to see if there is a session with the requested session_id
        try:
            session_value = (session_id)
            search_query = "SELECT * FROM WorkoutSessions WHERE session_id = (%s)"
            cursor.execute(search_query, session_value)
            if cursor.fetchone():
                print(f"There was workout session found with id of \'{session_id}\'!")
                return
        except:
            print("Problem searching for session")
            cursor.close()
            conn.close()
            return
        # Try to delete teh session by session_id
        try:
            query = "DELETE FROM WorkoutSessions WHERE session_id = (%s)"
            cursor.execute(query, session_value)
            conn.commit()
            print(f"Workout Session \'{session_id}\' delted!")
        finally:
            cursor.close()
            conn.close()

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