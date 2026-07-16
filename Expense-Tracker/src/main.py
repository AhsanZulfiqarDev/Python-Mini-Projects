"""
     main.py

Entry point of the Expense Tracker application.
"""

# Import ExpenseTracker class
from tracker import ExpenseTracker


def display_menu():
    """
    Display the main menu.
    """

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Monthly Summary")
    print("7. Exit")
    print("=====================================")


def main():
    """
    Main function of the program.
    """

    # Create ExpenseTracker object
    tracker = ExpenseTracker("data/expenses.json")

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        # ---------------- ADD EXPENSE ---------------- #

        if choice == "1":

            try:
                amount = float(input("Enter Amount: "))
            except ValueError:
                print("Invalid amount!")
                continue

            category = input("Enter Category: ")
            description = input("Enter Description: ")

            date = input("Enter Date (YYYY-MM-DD) or press Enter for today: ")

            if date == "":
                date = None

            tracker.add_expense(
                amount,
                category,
                description,
                date
            )

        # ---------------- VIEW ---------------- #

        elif choice == "2":

            tracker.view_expenses()

        # ---------------- SEARCH ---------------- #

        elif choice == "3":

            keyword = input("Enter category or description: ")

            tracker.search_expense(keyword)

        # ---------------- UPDATE ---------------- #

        elif choice == "4":

            tracker.view_expenses()

            try:

                expense_id = int(input("Expense ID: "))

                amount = float(input("New Amount: "))

            except ValueError:

                print("Invalid input!")

                continue

            category = input("New Category: ")

            description = input("New Description: ")

            date = input("New Date (YYYY-MM-DD): ")

            tracker.update_expense(
                expense_id,
                amount,
                category,
                description,
                date
            )

        # ---------------- DELETE ---------------- #

        elif choice == "5":

            tracker.view_expenses()

            try:

                expense_id = int(input("Expense ID to delete: "))

            except ValueError:

                print("Invalid ID!")

                continue

            tracker.delete_expense(expense_id)

        # ---------------- SUMMARY ---------------- #

        elif choice == "6":

            tracker.monthly_summary()

        # ---------------- EXIT ---------------- #

        elif choice == "7":

            print("\nThank you for using Expense Tracker!")

            break

        # ---------------- INVALID ---------------- #

        else:

            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()  
                
                     
    


