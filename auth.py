# auth.py
import sqlite3
import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user_table():
    """Create the users table if it doesn't exist."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    """Register a new user with a hashed password."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print(f"User {username} registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    """Authenticate a user by checking their username and hashed password."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Hash the provided password
    hashed_password = hash_password(password)

    # Retrieve the stored hashed password from the database
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    
    if result is None:
        print("Username not found.")
        return False

    stored_hashed_password = result[0]

    # Compare the provided hashed password with the stored hashed password
    if stored_hashed_password == hashed_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False

# Example usage
if __name__ == "__main__":
    create_user_table()
    register_user("john_doe", "securepassword")
    authenticate_user("john_doe", "securepassword")  # Should return True
    authenticate_user("john_doe", "wrongpassword")   # Should return False
