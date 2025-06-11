import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import crud


def main():
    print("=== Kutubxona Boshqaruv Tizimi ===")
    while True:
        role = input("\nKirish turi (1-Admin, 2-Foydalanuvchi, 0-Chiqish): ")

        if role == "1":
            crud.admin_menu()
        elif role == "2":
            crud.user_menu()
        elif role == "0":
            print("Chiqildi.")
            break
        else:
            print("Notogri tanlov.")

if __name__ == "__main__":
    main()

