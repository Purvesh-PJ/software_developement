# finance_manager/__init__.py
import datetime
from .transaction import Transaction
from .category import Category
from .report import Report


def main():
    categories = {}

    while True:
        print("\nFinance Manager")
        print("1. Add Transaction")
        print("2. Generate Report")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category_name = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description (optional): ")

            if category_name not in categories:
                categories[category_name] = Category(category_name)

            transaction = Transaction(amount, category_name, date, description)
            categories[category_name].add_transaction(transaction)

            print("Transaction added successfully!")

        elif choice == '2':
            report = Report(categories.values())
            print(report.generate())

        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
