from core.database_settings import execute_query

# ADMIN MENU 
def admin_menu():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Muallif qo'shish")
        print("2. Kitob qo'shish")
        print("3. Foydalanuvchilar ro'yxati")
        print("4. Barcha ijaralar")
        print("5. Statistika")
        print("0. Orqaga")

        choice = input("Tanlang: ")

        if choice == "1":
            full_name = input("Muallif ismi: ")
            execute_query("INSERT INTO authors(full_name) VALUES (%s);", (full_name,))
            print("Muallif qo'shildi.")
        elif choice == "2":
            title = input("Kitob nomi: ")
            author_id = int(input("Muallif ID: "))
            published_at = input("Nashr sanasi (YYYY-MM-DD): ")
            total = int(input("Jami nusxa: "))
            execute_query("""
                INSERT INTO books(title, author_id, published_at, total_count, available_count)
                VALUES (%s, %s, %s, %s, %s);
            """, (title, author_id, published_at, total, total))
            print("Kitob qo'shildi.")
        elif choice == "3":
            rows = execute_query("SELECT * FROM users;", fetch="all")
            for user in rows:
                print(f"{user['id']} - {user['full_name']} ({user['email']})")
        elif choice == "4":
            rows = execute_query("""
                SELECT b.id, u.full_name, bk.title, b.borrowed_at, b.returned_at
                FROM borrows b
                JOIN users u ON b.user_id = u.id
                JOIN books bk ON b.book_id = bk.id
                ORDER BY b.borrowed_at DESC;
            """, fetch="all")
            for row in rows:
                print(f"{row['id']} - {row['full_name']} - {row['title']} - {row['borrowed_at']} - {row['returned_at']}")
        elif choice == "5":
            # Example statistic: most borrowed books
            rows = execute_query("""
                SELECT bk.title, COUNT(*) AS borrow_count
                FROM borrows b
                JOIN books bk ON b.book_id = bk.id
                GROUP BY bk.title
                ORDER BY borrow_count DESC;
            """, fetch="all")
            print("Eng ko'p ijaraga olingan kitoblar:")
            for row in rows:
                print(f"{row['title']} - {row['borrow_count']} marta")
        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov.")

#  USER MENU
def user_menu():
    user_id = int(input("Foydalanuvchi ID-ni kiriting: "))  

    while True:
        print("\n--- Foydalanuvchi Paneli ---")
        print("1. Kitoblar ro'yxati")
        print("2. Muallif bo'yicha qidirish")
        print("3. Kitobni ijaraga olish")
        print("4. Kitobni qaytarish")
        print("5. Mening ijaralarim")
        print("0. Orqaga")

        choice = input("Tanlang: ")

        if choice == "1":
            books = execute_query("""
                SELECT b.id, b.title, a.full_name, b.available_count
                FROM books b JOIN authors a ON b.author_id = a.id;
            """, fetch="all")
            for b in books:
                print(f"{b['id']} - {b['title']} ({b['full_name']}) - Qolgan: {b['available_count']}")
        elif choice == "2":
            name = input("Muallif ismi: ")
            books = execute_query("""
                SELECT b.title, b.available_count
                FROM books b
                JOIN authors a ON b.author_id = a.id
                WHERE a.full_name ILIKE %s;
            """, (f"%{name}%",), fetch="all")
            for b in books:
                print(f"{b['title']} - Qolgan: {b['available_count']}")
        elif choice == "3":
            book_id = int(input("Kitob ID: "))
            # check availability
            book = execute_query("SELECT available_count FROM books WHERE id = %s;", (book_id,), fetch="one")
            if book and book['available_count'] > 0:
                execute_query("INSERT INTO borrows(user_id, book_id) VALUES (%s, %s);", (user_id, book_id))
                execute_query("UPDATE books SET available_count = available_count - 1 WHERE id = %s;", (book_id,))
                print("Kitob ijaraga olindi.")
            else:
                print("Bu kitob hozircha mavjud emas.")
        elif choice == "4":
            book_id = int(input("Kitob ID: "))
            execute_query("""
                UPDATE borrows SET returned_at = CURRENT_TIMESTAMP
                WHERE user_id = %s AND book_id = %s AND returned_at IS NULL;
            """, (user_id, book_id))
            execute_query("UPDATE books SET available_count = available_count + 1 WHERE id = %s;", (book_id,))
            print("Kitob qaytarildi.")
        elif choice == "5":
            rows = execute_query("""
                SELECT bk.title, b.borrowed_at, b.returned_at
                FROM borrows b
                JOIN books bk ON b.book_id = bk.id
                WHERE b.user_id = %s
                ORDER BY b.borrowed_at DESC;
            """, (user_id,), fetch="all")
            for row in rows:
                print(f"{row['title']} - {row['borrowed_at']} - {'Qaytarilgan' if row['returned_at'] else 'Ijara davomida'}")
        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov.")
