"""
file_handler.py

Handles saving and loading expense data
from a JSON file.
"""

# Built-in library for working with JSON files
import json

# Allows checking whether a file exists
import os

# Import the Expense class
from expense import Expense


class FileHandler:
    """
    Handles reading and writing expense data.
    """

    @staticmethod
    def save_expenses(expenses, filename):
        """
        Save a list of Expense objects to a JSON file.

        Parameters
        ----------
        expenses : list
            List of Expense objects.

        filename : str
            Path to the JSON file.
        """

        # Convert every Expense object into a dictionary
        data = [expense.to_dict() for expense in expenses]

        # Open the file in write mode
        with open(filename, "w") as file:

            # Save the list of dictionaries into the JSON file
            json.dump(data, file, indent=4)

    @staticmethod
    def load_expenses(filename):
        """
        Load expenses from a JSON file.

        Parameters
        ----------
        filename : str
            Path to the JSON file.

        Returns
        -------
        list
            List of Expense objects.
        """

        # If the file does not exist,
        # return an empty list
        if not os.path.exists(filename):
            return []

        # Open the JSON file in read mode
        with open(filename, "r") as file:

            # Convert JSON data into a Python list
            data = json.load(file)

        # Convert dictionaries back into Expense objects
        expenses = [
            Expense.from_dict(item)
            for item in data
        ]

        return expenses
    
    
    
    