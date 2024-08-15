# test_auth.py
import hashlib

# Simulate a simple in-memory database
users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    hashed_password = hash_password(password)
    users_db[username] = hashed_password
    print(f"User {username} registered successfully.")

def authenticate_user(username, password):
    hashed_password = hash_password(password)
    stored_hashed_password = users_db.get(username)

    if stored_hashed_password == hashed_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False

# Example usage
if __name__ == "__main__":
    register_user("john_doe", "securepassword")
    authenticate_user("john_doe", "securepassword")  # Should return True
    authenticate_user("john_doe", "wrongpassword")   # Should return False
