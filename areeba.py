# A simple dictionary to store user credentials (username: password)
database = {}

def signup():
    print("\n--- SIGNUP ---")
    username = input("Create a username: ")
    
    if username in database:
        print("Username already exists! Try a different one.")
    else:
        password = input("Create a password: ")
        database[username] = password
        print("Account created successfully!")

def login():
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in database and database[username] == password:
        print("Login successful! Welcome.")
    else:
        print("Invalid username or password.")

# Main Program Loop
while True:
    print("\n=== LOGIN & SIGNUP SYSTEM ===")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")