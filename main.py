import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from users.views import register, login
from core.table_queries import initializing_tables
import crud  

current_user = None

def auth_menu():
    global current_user

    while True:
        print("\nWelcome to the authentication menu!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user == "admin":
                current_user = "admin"
                return crud.admin_menu()
            elif user:
                current_user = user
                return crud.user_menu()
            else:
                continue
        elif choice == '3':
            print("Exiting")
            exit()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    initializing_tables()
    auth_menu()






