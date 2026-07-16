"""
tracker.py

Contains the ExpenseTracker class.

This class manages all expense operations.
"""

# Import the Expense class
from expense import Expense

# Import the FileHandler class
from file_handler import FileHandler


class ExpenseTracker:
    """
    Manages all expense operations.
    """

    def __init__(self, filename):
        """
        Initialize the Expense Tracker.

        Parameters
        ----------
        filename : str
            Path to the JSON file.
        """

        # Store filename
        self.filename = filename

        # Load expenses from the JSON file
        self.expenses = FileHandler.load_expenses(filename)

    def add_expense(self, amount, category, description, date=None):
        """
        Add a new expense.
        """

        # Create a new Expense object
        expense = Expense(amount, category, description, date)

        # Add the expense to the list
        self.expenses.append(expense)

        # Save updated data
        FileHandler.save_expenses(self.expenses, self.filename)

        print("\nExpense added successfully!\n")

    def view_expenses(self):
        """
        Display all expenses.
        """

        # Check if there are any expenses
        if len(self.expenses) == 0:
            print("\nNo expenses found.\n")
            return

        print("\n========== ALL EXPENSES ==========\n")

        # Display each expense
        for index, expense in enumerate(self.expenses, start=1):
            print(f"Expense ID : {index}")
            expense.display()

        print("=" * 50)

    def search_expense(self, keyword):
        """
        Search expenses by category or description.
        """

        found = False

        keyword = keyword.lower()

        print("\n========== SEARCH RESULTS ==========\n")

        for index, expense in enumerate(self.expenses, start=1):

            if (
                keyword in expense.category.lower()
                or keyword in expense.description.lower()
            ):

                print(f"Expense ID : {index}")
                expense.display()

                found = True

        if not found:
            print("No matching expense found.")

    def update_expense(self, expense_id, amount, category, description, date):
        """
        Update an existing expense.
        """

        # Validate expense ID
        if expense_id < 1 or expense_id > len(self.expenses):
            print("\nInvalid Expense ID.\n")
            return

        # Get the selected expense
        expense = self.expenses[expense_id - 1]

        # Update values
        expense.amount = amount
        expense.category = category
        expense.description = description
        expense.date = date

        # Save changes
        FileHandler.save_expenses(self.expenses, self.filename)

        print("\nExpense updated successfully!\n")

    def delete_expense(self, expense_id):
        """
        Delete an expense.
        """

        # Validate expense ID
        if expense_id < 1 or expense_id > len(self.expenses):
            print("\nInvalid Expense ID.\n")
            return

        # Remove expense
        deleted_expense = self.expenses.pop(expense_id - 1)

        # Save updated list
        FileHandler.save_expenses(self.expenses, self.filename)

        print(
            f"\nExpense '{deleted_expense.description}' deleted successfully!\n"
        )

    def monthly_summary(self):
        """
        Display total expenses by category.
        """

        # Check if expenses exist
        if len(self.expenses) == 0:
            print("\nNo expenses available.\n")
            return

        summary = {}

        total = 0

        # Calculate category totals
        for expense in self.expenses:

            if expense.category in summary:
                summary[expense.category] += expense.amount
            else:
                summary[expense.category] = expense.amount

            total += expense.amount

        print("\n========== MONTHLY SUMMARY ==========\n")

        # Display category totals
        for category, amount in summary.items():
            print(f"{category:<15} PKR {amount}")

        print("-" * 35)

        print(f"{'Total':<15} PKR {total}")

        print("=" * 35)               
         
     
             
    