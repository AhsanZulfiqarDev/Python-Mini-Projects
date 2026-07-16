"""
expense.py

This file contains the Expense class.

An Expense object represents ONE expense entered by the user.
"""

# Import datetime so we can automatically use today's date
from datetime import datetime


class Expense:
    """
    Represents a single expense.
    """

    def __init__(self, amount, category, description, date=None):
        """
        Initialize a new Expense object.

        Parameters
        ----------
        amount : float
            Expense amount.
        category : str
            Expense category.
        description : str
            Short description of the expense.
        date : str, optional
            Date of the expense. If not provided,
            today's date will be used.
        """

        self.amount = amount
        self.category = category
        self.description = description

        # If no date is provided, use today's date
        if date is None:
            self.date = datetime.today().strftime("%Y-%m-%d")
        else:
            self.date = date

    def display(self):
        """
        Display the expense in a readable format.
        """

        print("-" * 50)
        print(f"Date        : {self.date}")
        print(f"Category    : {self.category}")
        print(f"Description : {self.description}")
        print(f"Amount      : PKR {self.amount}")
        print("-" * 50)

    def to_dict(self):
        """
        Convert the Expense object into a dictionary.

        JSON cannot save Python objects directly,
        so we convert the object into a dictionary first.
        """

        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create an Expense object from a dictionary.

        Parameters
        ----------
        data : dict
            Dictionary containing expense information.

        Returns
        -------
        Expense
            A new Expense object.
        """

        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"]
        )    
            
        
        
        
        
        
        





