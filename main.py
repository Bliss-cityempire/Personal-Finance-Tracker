from finance_tracker import FinanceTracker
from visualize import plot_expenses, plot_expenses_vs_income  # Import visualization functions
from auth import create_user_table, register_user, authenticate_user  # Import authentication functions

def main():
    create_user_table()  # Ensure the user table is created

    print("Welcome to Personal Finance Tracker!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
            print("User registered successfully!")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate_user(username, password):
                print("Login successful!")
                break
            else:
                print("Invalid credentials. Please try again.")

        elif choice == '3':
            print("Exiting...")
            return

        else:
            print("Invalid choice, please try again.")
    
    # Once the user is authenticated, they can access the tracker functionalities
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View Expense Chart")
        print("4. View Income vs. Expenses Chart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Rent): ")
            description = input("Enter description (optional): ")
            tracker.add_transaction(amount, category, description)
            print("Transaction added!")

        elif choice == '2':
            summary = tracker.get_summary()
            print(f"\nIncome: {summary['income']}")
            print(f"Expenses: {summary['expenses']}")
            print(f"Balance: {summary['balance']}")

        elif choice == '3':
            plot_expenses()  # Call the expense chart function

        elif choice == '4':
            plot_expenses_vs_income()  # Call the income vs. expenses function

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
