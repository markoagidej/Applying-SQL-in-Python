# 1. Gym Database Management with Python and SQL

import mysql.connector
from mysql.connector import Error

def connect_db():
    # Connect to DB and return the connection
    try:
        conn = mysql.connector.connect("applying_sql_in_python", "root", "PASSWORD", "HOST")
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
def update_member_age():
    pass

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    pass

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
            update_member_age()
        elif choice == 4: # Delete Workout Session
            delete_workout_session(session_id)
        elif choice == 5:
            print("Thank you, goodbye!")
            exit()


if __name__ == "__main__":
    main()