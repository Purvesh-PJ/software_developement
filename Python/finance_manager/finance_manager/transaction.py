# finance_manager/transaction.py

class Transaction:
    def __init__(self, amount, category, date, description=''):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __repr__(self):
        return f"Transaction(amount={self.amount}, category='{self.category}', date='{self.date}', description='{self.description}')"
