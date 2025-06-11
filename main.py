import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import crud



def login_menu():
    print("=== Kutubxona Tizimiga Xush kelibsiz ===")
    print("1. Admin sifatida kirish")
    print("2. Foydalanuvchi sifatida kirish")
    choice = input("Tanlang (1/2): ")

    if choice == '1':
        email = input("Admin email: ").strip()
        password = input("Parol: ").strip()
       
        if email == "admin@kutubxona.uz" and password == "admin123":
            print("Admin sifatida tizimga kirdingiz.")
            crud.admin_menu()
        else:
            print("Xato! Email yoki parol noto‘g‘ri.")
    elif choice == '2':
        name = input("Ismingizni kiriting: ").strip()
        print(f"Xush kelibsiz, {name}!")
        crud.user_menu()
    else:
        print("Notogri tanlov.")

if __name__ == "__main__":
    login_menu()



