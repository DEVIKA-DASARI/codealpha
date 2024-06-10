import csv
from datetime import datetime

# File where expenses will be stored
EXPENSES_FILE = 'expenses.csv'

# Function to add a new expense
def add_expense(date, category, amount, description):
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print(f"Expense added: {date}, {category}, {amount}, {description}")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("Date, Category, Amount, Description")
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No expenses found. Add some expenses first.")

# Function to view expenses by category
def view_expenses_by_category(category):
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            print(f"Expenses for category: {category}")
            print("Date, Amount, Description")
            for row in reader:
                if row[1] == category:
                    print(f"{row[0]}, {row[2]}, {row[3]}")
    except FileNotFoundError:
        print("No expenses found. Add some expenses first.")

# Function to get total expenses
def get_total_expenses():
    total = 0
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
    except FileNotFoundError:
        print("No expenses found. Add some expenses first.")
    print(f"Total expenses: {total}")

# Main function to run the expense tracker
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Get Total Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category = input("Enter category: ")
            view_expenses_by_category(category)
        elif choice == '4':
            get_total_expenses()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the expense tracker
if __name__ == "__main__":
    main()
