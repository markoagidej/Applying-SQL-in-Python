# 1. Gym Database Management with Python and SQL

# Task 1: Add a Member

# Task 2: Add a Workout Session

# Task 3: Updating Member Information

# Task 4: Delete a Workout Session

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

        if choice == 1:
            add_member()
        elif choice == 2:
            add_workout_session()
        elif choice == 3:
            update_member_age()
        elif choice == 4:
            delete_workout_session(session_id)
        elif choice == 5:
            print("Thank you, goodbye!")
            exit()


if __name__ == "__main__":
    main()