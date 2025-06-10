from core.database_settings import execute_query
from core.database_settings import execute_query

authors = """
            CREATE TABLE IF NOT EXISTS authors (
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(255) NOT NULL
            );

           """


users = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL
            );
           """


books = """
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author_id INTEGER REFERENCES authors(id),
                published_at DATE,
                total_count INTEGER NOT NULL,
                available_count INTEGER NOT NULL
            );
           """ 

borrows = """
            CREATE TABLE IF NOT EXISTS borrows (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                book_id INTEGER REFERENCES books(id),
                borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                returned_at TIMESTAMP NULL
            );
           """







