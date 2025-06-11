from core.database_settings import execute_query
admin_login = "admin"
admin_email = "admin@123gmail.com"

def register():
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    

    check_query = "SELECT * FROM users WHERE full_name = %s;"
    existing = execute_query(query=check_query, params=(full_name,), fetch="one")
    if existing:
        print("Username already exists!")
        return

    insert_query = """
        INSERT INTO users (full_name, email )
        VALUES (%s, %s);
    """
    execute_query(query=insert_query, params=(full_name,email))
    print("Registration successful!")

def login():
    full_name = input("Enter full name: ")
    email= input("Enter email: ")

    if full_name == admin_login and email == admin_email:
        print("Admin login successful!")
        return "admin"
    query = "SELECT id FROM users WHERE full_name = %s AND email = %s;"
    user = execute_query(query=query, params=(full_name, email), fetch="one")


    if user:
        user_id = user[0]
        update_query = "UPDATE users SET is_login = TRUE WHERE id = %s;"
        execute_query(query=update_query, params=(user_id,))
        print("Login successful!")
        return user_id
    else:
        print("Invalid credentials!")
        return None